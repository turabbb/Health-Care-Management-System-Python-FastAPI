from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.api.deps import get_current_staff, get_current_user
from app.crud.crud_patient import patient
from app.schemas.patient import Patient, PatientCreate, PatientUpdate
from app.schemas.user import User
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=List[Patient])
def read_patients(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_staff),
) -> Any:
    """
    Retrieve patients.
    """
    patients = patient.get_multi(db, skip=skip, limit=limit)
    return patients

@router.post("/", response_model=Patient)
def create_patient(
    *,
    db: Session = Depends(get_db),
    patient_in: PatientCreate,
    current_user: User = Depends(get_current_staff),
) -> Any:
    """
    Create new patient.
    """
    existing_patient = patient.get_by_email(db,email=patient_in.email)
    if existing_patient:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The patient with this email already exists in the system.",
        )

    try:
        patient_obj = patient.create(db, obj_in=patient_in)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The patient with this email already exists in the system."
        )
    return patient_obj

@router.get("/{id}", response_model=Patient)
def read_patient(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: User = Depends(get_current_user),
) -> Any:
    """
    Get patient by ID.
    """
    patient_obj = patient.get(db, id=id)
    if not patient_obj:
        raise HTTPException(status_code=404, detail="Patient not found")

    if current_user.role == "patient" and current_user.reference_id != id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    return patient_obj

@router.put("/{id}", response_model=Patient)
def update_patient(
    *,
    db: Session = Depends(get_db),
    id: int,
    patient_in: PatientUpdate,
    current_user: User = Depends(get_current_staff),
) -> Any:
    """
    Update a patient.
    """
    patient_obj = patient.get(db, id=id)
    if not patient_obj:
        raise HTTPException(status_code=404, detail="Patient not found")

    if patient_in.email and patient_in.email != patient_obj.email:
        existing_patient = patient.get_by_email(db, email=patient_in.email)
        if existing_patient and existing_patient.id != id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The email is already registered to another patient."
            )

    patient_obj = patient.update(db, db_obj=patient_obj, obj_in=patient_in)
    return patient_obj

@router.delete("/{id}", response_model=Patient)
def delete_patient(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: User = Depends(get_current_staff),
) -> Any:
    """
    Delete a patient.
    """
    patient_obj = patient.get(db, id=id)
    if not patient_obj:
        raise HTTPException(status_code=404, detail="Patient not found")

    patient_obj = patient.remove(db, id=id)
    return patient_obj

@router.get("/search/", response_model=List[Patient])
def search_patients(
    *,
    db: Session = Depends(get_db),
    query: str = Query(..., min_length=3),
    current_user: User = Depends(get_current_staff),
) -> Any:
    """
    Search for patients by name or email.
    """
    patients = patient.search(db, query=query)
    return patients
