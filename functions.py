class DiagnosisStatus(str, Enum):
    ACTIVE = "active"
    RESOLVED = "resolved"
    POST_REPAIR = "post-repair"
    STABLE = "stable"
    PROGRESSIVE = "progressive"
    UNKNOWN = "unknown"

class SelectedCode(BaseModel):
    code: Optional[str] = Field(
        None,
        description="Selected ontology code (may be null if model returned null)."
    )
    name: Optional[str] = Field(
        None,
        description="Selected ontology concept name/label (may be null if model returned null)."
    )

class DiagnosisItem(BaseModel):
    """Individual diagnosis entry with date and status."""
    diagnosis: str = Field(
        ...,
        description="Name of the cardiac diagnosis (e.g., Tetralogy of Fallot, DORV, cardiomyopathy). Ensure that you extract one diagnosis at a time and only those that are explicitly identified. Do not extract things that have either been ruled out by the study or cannot be ruled out."
    )
    date_of_diagnosis: Optional[str] = Field(
        None,
        description="Approximate or known date of diagnosis if available (format: YYYY-MM or YYYY-MM-DD)."
    )
    status: Optional[str] = Field(
        None,
        description="Current status of the diagnosis (e.g., active, resolved, post-repair, stable, progressive)."
    )
    SNOMEDdx_SELECTED: Optional[SelectedCode] = Field(
        None,
        description="Final selected SNOMED diagnosis code for this diagnosis (post-retrieval selection)."
    )
    IPCCCshort_SELECTED: Optional[SelectedCode] = Field(
        None,
        description="Final selected IPCCC short diagnosis code for this diagnosis (post-retrieval selection)."
    )
    IPCCClong_SELECTED: Optional[SelectedCode] = Field(
        None,
        description="Final selected IPCCC long diagnosis code for this diagnosis (post-retrieval selection)."
    )


class SurgicalIntervention(BaseModel):
    """Details of a surgical or interventional procedure."""
    procedure_name: str = Field(
        ...,
        description="Name or description of the cardiac-specific surgical or interventional procedure performed. If multiple procedures/interventions performed at once, extract each one separately."
    )
    date_of_procedure: Optional[str] = Field(
        None,
        description="Approximate or known date of the procedure (format: YYYY-MM or YYYY-MM-DD)."
    )
    SNOMEDproc_SELECTED: Optional[SelectedCode] = Field(
        None,
        description="Final selected SNOMED procedure code for this procedure (post-retrieval selection)."
    )

    
# Surgical / Device History / Other

class SurgicalHistory(BaseModel):
    """Surgical or interventional history."""
    prior_surgical_interventions: Optional[List[SurgicalIntervention]] = Field(
        None, 
        description="Details of previous surgeries or repairs. Include the date of the surgery, procedure, or repair for each one if present. Do not include noncardiac procedures. Ensure that you extract one diagnosis at a time and only those that are explicitly identified (ie. subaortic membrane resection and valve repair should be 2 separate procedures)."
    )


class DiagnosisHistory(BaseModel):
    """Prior or current cardiac diagnoses."""
    cardiac_diagnoses: Optional[List[DiagnosisItem]] = Field(
        None,
        description="List of prior and current cardiac diagnoses with their respective dates, status, and source references. Do not include noncardiac diagnoses, such as genetic conditions."
    )
   
#
# 4) TOP-LEVEL ECHO REPORT MODEL
#

class EchoReport(BaseModel):
    """Main Pydantic model capturing the full echo report."""

    # Additional structural/surgical/device data
    diagnoses: Optional[DiagnosisHistory] = None
    surgical_history: Optional[SurgicalHistory] = None

    class Config:
        # If you prefer enum field values as strings in the JSON output:
        use_enum_values = True
        extract_json= {
            "example": {
                "atria": {
                    "RA": {"RA_dilation": "Mild"},
                    "LA": {
                        "LA_dilation": "Moderate",
                        "LA_volume_indexed": {
                            "numeric": 35.0,
                            "unit": "mL/m^2"
                        }
                    }
                },
                "ventricles": {
                    "RV": {
                        "RV_size_structure": {
                            "RV_dilation": "Normal",
                            "RV_hypertrophy": "No"
                        },
                        "RV_function": {
                            "RV_systolic_function": "Normal"
                        }
                    },
                    "LV": {
                        "LV_size_structure": {
                            "LV_dilation": "Mild",
                            "LV_hypertrophy": "Mild",
                            "LV_volume_systole": {
                                "numeric": 50.0,
                                "unit": "mL"
                            },
                            "LV_volume_diastole": {
                                "numeric": 120.0,
                                "unit": "mL"
                            }
                        },
                        "LV_function": {
                            "LV_systolic_function": "Normal",
                            "LVEF": {
                                "numeric": 60.0,
                                "unit": "%"
                            }
                        }
                    }
                },
                "valves": {
                    "tricuspid": {
                        "TV_structural_status": "Structurally normal",
                        "TV_regurgitation_severity": "Mild"
                    },
                    "pulmonary": {
                        "PV_annulus_size": {
                            "numeric": 18.0,
                            "unit": "mm"
                        },
                        "PV_stenosis_severity": "No",
                        "PV_structural_status": "Structurally normal",
                        "PV_regurgitation_severity": "Trace/Trivial"
                    },
                    "mitral": {
                        "MV_stenosis_severity": "No",
                        "MV_structural_status": "Structurally normal",
                        "MV_regurgitation_severity": "Mild"
                    },
                    "aortic": {
                        "AV_structural_status": "Structurally normal",
                        "AV_leaflets": 3,
                        "AV_stenosis_severity": "No",
                        "AV_regurgitation_severity": "No"
                    }
                },
                "great_vessels": {
                    "aorta": {
                        "arch_sidedness": "Left",
                        "aortic_root_size": {
                            "numeric": 28.0,
                            "unit": "mm"
                        },
                        "ascending_aorta_diameter": {
                            "numeric": 30.0,
                            "unit": "mm"
                        },
                        "aortic_isthmus_size": {
                            "numeric": 18.0,
                            "unit": "mm"
                        },
                        "coarctation": False
                    }
                },
                "pHTN": {
                    "severity": "None",
                    "TR_jet_gradient": {
                        "numeric": 20.0,
                        "unit": "mmHg"
                    },
                    "IVS_flattening_in_systole": False
                },
                "asd": {
                    "atrial_communication_present": True,
                    "asd_types": ["PFO", "Secundum"],
                    "asd_size": "Small",
                    "asd_direction_of_flow": "Left to right"
                },
                "vsd": {
                    "ventricular_communication_present": True,
                    "vsd_types": ["PERIMEMBRANOUS", "MID_MUSCULAR"],
                    "vsd_size": "Moderate",
                    "vsd_direction_of_flow": "Left to right",
                    "vsd_peak_gradient": {
                        "numeric": 40,
                        "unit": "mmHg"
                    }
                },
                "pda": {
                    "present": False
                },
                "CA": {
                    "LCA_structure":"Normal",
                    "RCA_structure": "Anomalous aortic origin of right coronary artery with right coronary artery originating from left aortic sinus"
                },
                "surgical_history": {
                    "prior_surgical_interventions": "No prior surgeries"
                }
            }
        }
