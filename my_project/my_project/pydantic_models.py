from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


#
# 1) SUBMODEL FOR ANY NUMERIC FIELD
#

class Z_score_of_reported_numeric(BaseModel):
    z_score: Optional[float] = Field(
        None,
        description="Z-score for the measurement, if available. Represents the number of standard deviations a value is from the mean of a reference population."
    )
    type_of_z_score: Optional[str] = Field(
        None,
        description="Type of z-score used (e.g., 'age-adjusted', 'sex-adjusted', 'population-based', 'Boston', 'PHN', etc.)."
    )


class NumericValue(BaseModel):
    numeric: Optional[float] = Field(
        None,
        description="Numeric measurement value."
    )
    unit: Optional[str] = Field(
        None,
        description="Unit of measurement (e.g., mm, cm, m/s, mmHg, etc.)."
    )
    z_score: Optional[List[Z_score_of_reported_numeric]] = Field(
        None,
        description="Z-score(s) for the measurement, if available."
    )

#
# 2) ENUMS FOR QUALITATIVE DATA
#

class Bool_with_Other(str, Enum):
    TRUE = "True or yes"
    FALSE = "False or No"
    OTHER = "Other"

class DilationSeverity(str, Enum):
    APLASTIC = "Aplastic"
    HYPOPLASTIC = "Hypoplastic"
    SMALL = "Small"
    NORMAL = "Normal"
    MILD = "Mild dilation"
    MILD_MODERATE = "Mild-Moderate dilation"
    MODERATE = "Moderate dilation"
    MODERATE_SEVERE = "Moderate-Severe dilation"
    SEVERE = "Severe dilation"
    OTHER = "Other"

class HypertrophySeverity(str, Enum):
    NO = "No"
    MILD = "Mild hypertrophy"
    MILD_MODERATE = "Mild-Moderate hypertrophy"
    MODERATE = "Moderate hypertrophy"
    MODERATE_SEVERE = "Moderate-Severe hypertrophy"
    SEVERE = "Severe hypertrophy"
    OTHER = "Other type of hypertrophy"

class StenosisSeverity(str, Enum):
    NO = "No"
    TRACE_TRIVIAL = "Trace/Trivial"
    MILD = "Mild"
    MILD_MODERATE = "Mild-Moderate"
    MODERATE = "Moderate"
    MODERATE_SEVERE = "Moderate-Severe"
    SEVERE = "Severe"

class RegurgitationSeverity(str, Enum):
    NO = "No"
    TRACE_TRIVIAL = "Trace/Trivial"
    MILD = "Mild"
    MILD_MODERATE = "Mild-Moderate"
    MODERATE = "Moderate"
    MODERATE_SEVERE = "Moderate-Severe"
    SEVERE = "Severe"

class StructuralStatus(str, Enum):
    NORMAL = "Structurally normal"
    ABNORMAL = "Structurally abnormal"

class SystolicDiastolicFunction(str, Enum):
    NORMAL = "Normal"
    LOW_NORMAL = "Low normal"
    MILDLY_DEPRESSED = "Mildly depressed"
    MILD_MODERATE_DEPRESSED = "Mild-Moderately depressed"
    MODERATELY_DEPRESSED = "Moderately depressed"
    MODERATE_SEVERE_DEPRESSED = "Moderate-Severely depressed"
    SEVERELY_DEPRESSED = "Severely depressed"
    AKINETIC = "Akinetic"
    HYPERDYNAMIC = "Hyperdynamic"
    OTHER = "Other"

class PressureSeverity(str, Enum):
    NORMAL = "Normal"
    MILD_ELEVATED = "Mildly elevated"
    MODERATE_ELEVATED = "Moderately elevated"
    SEVERE_ELEVATED = "Severely elevated"
    LESS_HALF_SYSTEMIC = "Less than half systemic"
    HALF_SYSTEMIC = "Half systemic"
    APPROACHING_SYSTEMIC = "Approaching systemic"
    SYSTEMIC = "Systemic"
    SUPRASYSTEMIC = "Suprasystemic"

class Size(str, Enum):
    TINY = "Tiny"
    SMALL = "Small"
    SMALL_MODERATE = "Small-moderate"
    MODERATE = "Moderate"
    MODERATE_LARGE = "Moderate-large"
    LARGE = "Large"

class ASD_type(str, Enum):
    SECUNDUM = "Secundum"
    PRIMUM = "Primum"
    PFO = "Patent Foramen Ovale"
    SUPERIOR_SINUS_VENOSUS = "Superior sinus venosus"
    CORONARY_SINUS = "Coronary sinus"
    SURGICAL = "Surgically created atrial septal defect"
    INFERIOR_SINUS_VENOSUS = "Inferior sinus venosus"
    OTHER = "Other"

class VSD_type(str, Enum):
    PERIMEMBRANOUS = "Perimembranous"
    ANTERIOR_MALALIGNMENT = "Anterior malalignment"
    POSTERIOR_MALALIGNMENT = "Posterior malalignment"
    MID_MUSCULAR = "Mid muscular"
    POSTERIOR_MUSCULAR = "Posterior muscular"
    APICAL_MUSCULAR = "Apical muscular"
    INLET = "Inlet"
    OUTLET_DOUBLY_COMMITTED = "Outlet/doubly-committed juxta-arterial"
    PERIMEMBRANOUS_INLET = "Perimembranous inlet"
    OUTLET_SUBAORTIC = "Outlet/subaortic"
    CONOVENTRICULAR = "Conoventricular"
    OTHER = "Other"

class Direction(str, Enum):
    ALL_LEFT_RIGHT = "Left to right"
    PREDOMINANTLY_LEFT_RIGHT = "Predominantly left to right"
    ALL_RIGHT_LEFT = "Right to left"
    PREDOMINANTLY_RIGHT_LEFT = "Predominantly right to left"
    BIDIRECTIONAL = "Bidirectional"

class Sidedness(str, Enum):
    LEFT = "Left"
    RIGHT = "Right"

class LCA(str, Enum):
    NORMAL = "Normal left coronary artery anatomy"
    L_FROM_R = "Anomalous aortic origin of left coronary artery with left coronary artery originating from right aortic sinus" 
    OTHER = "Other"

class RCA(str, Enum):
    NORMAL = "Normal right coronary artery anatomy"
    R_FROM_L = "Anomalous aortic origin of right coronary artery with right coronary artery originating from left aortic sinus" 
    OTHER = "Other"

class CA_abnormality(str, Enum):
    SINGLE = "Single coronary artery present"
    ABSENT = "Abscence of both coronary arteries"
    ACCESSORY = "Accessory coronary artery present"
    CA_STENOSIS = "Stenosis of coronary artery orifice/ostium"
    CA_ATRESIA = "Atresia of coronary artery orifice/ostium"
    CA_FISTULA = "Coronary artery fistula present"
    CA_ANEURYSM = "Coronary artery aneurysm present"

class RSVC(str, Enum):
    NORMAL = "Normal right SVC"
    ABSENT = "Absent right SVC"
    R_GLENN = "Right sided Glenn anastamosis"

class LSVC(str, Enum):
    LSVC_CS = "Left SVC draining to coronary sinus"
    LSVC_LA = "Left SVC draining to left atrium"
    ABSENT = "Absent left SVC" 
    L_GLENN = "Left sided Glenn anastamosis"

class IVC_option(str, Enum):
    NORMAL = "Normal IVC"
    INTERRUPTED = "Interrupted IVC"
    STENOTIC = "IVC Stenosis"
    OTHER = "Other"

class CardiacSitusEnum(str, Enum):
    solitus = "Situs solitus"              # Normal atrial arrangement
    inversus = "Situs inversus"            # Mirror-image atrial arrangement
    ambiguous = "Situs ambiguous"          # Heterotaxy / isomerism

class VentricularLoopingEnum(str, Enum):
    d_loop = "D-loop"                      # Morphologic RV on right
    l_loop = "L-loop"                      # Morphologic RV on left (ventricular inversion)
    
class CardiacPositionEnum(str, Enum):
    levocardia = "Levocardia"      # Heart apex pointing left (normal)
    dextrocardia = "Dextrocardia"  # Heart apex pointing right
    mesocardia = "Mesocardia"      # Heart apex pointing midline

class CardiacApexOrientationEnum(str, Enum):
    left = "Apex pointing left"
    right = "Apex pointing right"
    midline = "Apex pointing midline"

class DiagnosisStatus(str, Enum):
    ACTIVE = "active"
    RESOLVED = "resolved"
    POST_REPAIR = "post-repair"
    STABLE = "stable"
    PROGRESSIVE = "progressive"
    UNKNOWN = "unknown"

class DiagnosisItem(BaseModel):
    """Individual diagnosis entry with date and status."""
    diagnosis: str = Field(
        ...,
        description="Name of the cardiac diagnosis (e.g., Tetralogy of Fallot, DORV, cardiomyopathy). Do not include noncardiac diagnoses, such as genetic conditions, and "
    )
    date_of_diagnosis: Optional[str] = Field(
        None,
        description="Approximate or known date of diagnosis if available (format: YYYY-MM or YYYY-MM-DD)."
    )
    status: Optional[str] = Field(
        None,
        description="Current status of the diagnosis (e.g., active, resolved, post-repair, stable, progressive)."
    )
    source_text: Optional[str] = Field(
        None,
        description="Exact line or snippet of text from which the diagnosis was extracted. Provide the text from which it was extracted in a deidentified manner (e.g., do not include name, DOB, address)."
    )
    explainability: Optional[str] = Field(
        None,
        description="Brief explanation of how or why this diagnosis was identified from the text."
    )

class SurgicalIntervention(BaseModel):
    """Details of a surgical or interventional procedure."""
    procedure_name: str = Field(
        ...,
        description="Name or description of the cardiac-specific surgical or interventional procedure performed."
    )
    date_of_procedure: Optional[str] = Field(
        None,
        description="Approximate or known date of the procedure (format: YYYY-MM or YYYY-MM-DD)."
    )
    source_reference: Optional[str] = Field(
        None,
        description="Exact line of text or section from which this information was extracted. Provide the text from which it was extracted in a deidentified manner (e.g., do not include name, DOB, address)"
    )
    explainability: Optional[str] = Field(
        None,
        description="Brief explanation of how or why this procedure was identified from the text."
    )
    
#
# 3) DEFINE SUBMODELS FOR EACH ANATOMIC REGION
#

# Situs
class Situs(BaseModel):
    atrial_situs: Optional[CardiacSitusEnum] = Field(
        None, description="Arrangement of the atria [e.g. situs solitus (S), situs inversus (I), situs ambiguous (A) which may be denoted as the first letter from {S,D,S} segmental anatomy nomenclature]"
    )
    visceral_situs: Optional[CardiacSitusEnum] = Field(
        None, description="Visceral organ arrangement [e.g. situs solitus, situs inversus, situs ambiguous]"
    )
    heterotaxy: Optional[bool] = Field(
        None, description="True if report explicitly states heterotaxy syndrome or atrial isomerism"
    )
    heterotaxy_notes: Optional[str] = Field(
        None, description="Additional situs details, e.g., right atrial isomerism, left atrial isomerism"
    )
    ventricular_looping: Optional[VentricularLoopingEnum] = Field(
        None, description="Ventricular looping pattern (e.g. D or L looped ventricles)"
    )
    looping_notes: Optional[str] = Field(
        None, description="Additional details such as malposition or indeterminate morphology"
    )

class CardiacPosition(BaseModel):
    position: Optional[CardiacPositionEnum] = Field(
        None, description="Position of the heart within the thorax"
    )
    apex_orientation: Optional[CardiacApexOrientationEnum] = Field(
        None, description="Direction the cardiac apex is pointing"
    )
    position_notes: Optional[str] = Field(
        None, description="Additional details such as rotation or displacement"
    )


# Atria

class RA_info(BaseModel):
    """Right Atrium"""
    RA_dilated: Optional[bool] = Field(
        None,
        description="True if right atrium (RA) is dilated."
    )
    RA_dilation: Optional[DilationSeverity] = Field(
        None, 
        description="Describe degree of right atrial (RA) chamber size as commented on in the report (e.g. severely dilated, aplastic, hypoplastic)."
    )
    RA_dilation_other: Optional[str] = Field(
        None,
        description="If 'Other' was selected in RA_dilation, specify here."
    )
    
class LA_info(BaseModel):
    """Left Atrium"""
    LA_dilated: Optional[bool] = Field(
        None,
        description="True if left atrium (LA) is dilated."
    )    
    LA_dilation: Optional[DilationSeverity] = Field(
        None, 
        description="Describe degree of left atrial (LA) chamber size as commented on in the report (e.g. severely dilated, aplastic, hypoplastic)."
    )
    LA_dilation_other: Optional[str] = Field(
        None,
        description="If 'Other' was selected in LA_dilation, specify here."
    )
    LA_volume_indexed: Optional[NumericValue] = Field(
        None, 
        description="Left atrial (LA) volume measurement in systole (indexed)."
    )

class Atria(BaseModel):
    """Combined submodel for Atria"""
    RA: Optional[RA_info] = None
    LA: Optional[LA_info] = None
    Atrial_septum_gradient: Optional[NumericValue] = Field(
        None, 
        description="Gradient across the atrial septum in mmHg between the right and left atria. This can only be from an atrial communications, such as a PFO or ASD."
    )



# Ventricles

class RVSizeStructure(BaseModel):
    """Right ventricle size/structure details."""
    RV_dilated: Optional[bool] = Field(
        None,
        description="True if right ventricle (RV) is dilated."
    )    
    RV_dilation: Optional[DilationSeverity] = Field(
        None, 
        description="Describe degree of right ventricular (RV) chamber size as commented on in the report (e.g. severely dilated, aplastic, hypoplastic)."
    )
    RV_dilation_other: Optional[str] = Field(
        None,
        description="If 'Other' was selected in RV_dilation, specify here (e.g. RV dilated)."
    )
    RV_hypertrophy: Optional[HypertrophySeverity] = Field(
        None,
        description="Right ventricle (RV) hypertrophy presence/severity."
    )

class RVFunction(BaseModel):
    """Right ventricle functional details."""
    RV_systolic_function: Optional[SystolicDiastolicFunction] = Field(
        None,
        description="Qualitative right ventricular (RV) systolic function."
    )

class RV_info(BaseModel):
    """Combines size/structure and function for the RV."""
    RV_size_structure: Optional[RVSizeStructure] = None
    RV_function: Optional[RVFunction] = None


class LVSizeStructure(BaseModel):
    """Left ventricle size/structure details."""
    LV_dilated: Optional[bool] = Field(
        None,
        description="True if left ventricle (LV) is dilated."
    )    
    LV_dilation: Optional[DilationSeverity] = Field(
        None, 
        description="Describe the left ventricular (LV) chamber size as commented on in the report (e.g. severely dilated, aplastic, hypoplastic)."
    )
    LV_dilation_other: Optional[str] = Field(
        None,
        description="If 'Other' was selected in LV_dilation, specify here (e.g. LV dilated)."
    )
    LV_hypertrophy: Optional[HypertrophySeverity] = Field(
        None,
        description="Left ventricle (LV) hypertrophy presence/severity."
    )
    LV_volume_systole: Optional[NumericValue] = Field(
        None,
        description="Left ventricle (LV) volume in systole."
    )
    LV_volume_diastole: Optional[NumericValue] = Field(
        None,
        description="Left ventricle (LV) volume in diastole."
    )

class LVFunction(BaseModel):
    """Left ventricle functional details."""
    LV_systolic_function: Optional[SystolicDiastolicFunction] = Field(
        None,
        description="Qualitative LV systolic function."
    )
    LV_systolic_function_other: Optional[str] = Field(
        None,
        description="If LV_systolic_function is 'Other', specify here."
    )
    LVEF: Optional[NumericValue] = Field(
        None,
        description="Left Ventricular Ejection Fraction (e.g., Simpson's biplane)."
    )

class LV_info(BaseModel):
    """Combines size/structure and function for the LV."""
    LV_size_structure: Optional[LVSizeStructure] = None
    LV_function: Optional[LVFunction] = None


class Ventricles(BaseModel):
    """Container for both right and left ventricles."""
    RV: Optional[RV_info] = None
    LV: Optional[LV_info] = None


# Valves

class TricuspidValve(BaseModel):
    """Tricuspid valve details."""
    TV_structural_status: Optional[StructuralStatus] = Field(
        None,
        description="Structurally normal or abnormal tricuspid valve."
    )
    TV_structural_status_other: Optional[str] = Field(
        None,
        description="If TV_structural_status is 'abnormal', specify here."
    )
    TV_regurgitation_severity: Optional[RegurgitationSeverity] = Field(
        None,
        description="Tricuspid regurgitation presence/severity."
    )
    TV_annulus: Optional[NumericValue] = Field(
        None, 
        description="Tricuspid valve annulus size."
   )
    
class PulmonaryValve(BaseModel):
    """Pulmonary valve details."""
    PV_annulus_size: Optional[NumericValue] = Field(
        None,
        description="Pulmonary valve (or neo-pulmonary valve if pulmonary valve not available) annulus diameter/size."
    )
    PV_stenosis_severity: Optional[StenosisSeverity] = Field(
        None,
        description="Pulmonary valve (or neo-pulmonary valve if pulmonary valve not available) stenosis presence/severity."
    )
    PV_structural_status: Optional[StructuralStatus] = Field(
        None,
        description="Pulmonary valve (or neo-pulmonary valve if pulmonary valve not available) structure normal/abnormal."
    )
    PV_structural_status_other: Optional[str] = Field(
        None,
        description="If PV_structural_status is 'abnormal', specify here."
    )
    PV_regurgitation_severity: Optional[RegurgitationSeverity] = Field(
        None,
        description="Pulmonary valve (or neo-pulmonary valve if pulmonary valve not available) regurgitation severity."
    )
    PV_pressure_gradient: Optional[NumericValue] = Field(
        None,
        description="Peak pressure gradient across the pulmonary valve (or neo-pulmonary valve if pulmonary valve not available)."
    )
    RVOT_obstruction: Optional[bool] = Field(
        None,
        description="True if there is any RVOT obstruction."
    )
    RVOT_obstruction_dynamic: Optional[str] = Field(
        None,
        description="If RVOT_obstruction 'True': specify if dyanmic, fixed, or dynamic and fixed obstruction."
    )

class MitralValve(BaseModel):
    """Mitral valve details."""
    MV_stenosis_severity: Optional[StenosisSeverity] = Field(
        None,
        description="Mitral valve stenosis presence/severity."
    )
    MV_structural_status: Optional[StructuralStatus] = Field(
        None,
        description="Mitral valve structure normal/abnormal."
    )
    MV_structural_status_other: Optional[str] = Field(
        None,
        description="If MV_structural_status is 'abnormal', specify here."
    )
    MV_regurgitation_severity: Optional[RegurgitationSeverity] = Field(
        None,
        description="Mitral regurgitation presence/severity."
    )
    MV_annulus: Optional[NumericValue] = Field(
        None, 
        description="Mitral valve annulus size."
    )
    MV_EA_ratio: Optional[NumericValue] = Field(
        None, 
        description="Mitral valve E/A (also sometimes reported as E:A) wave ratio."
    )


class AorticValve(BaseModel):
    """Aortic valve details."""
    AV_structural_status: Optional[StructuralStatus] = Field(
        None,
        description="Aortic valve (or neo-aortic valve if aortic valve not available) structure normal/abnormal."
    )
    AV_structural_status_other: Optional[str] = Field(
        None,
        description="If AV_structural_status is 'abnormal', specify here."
    )
    AV_leaflets: Optional[int] = Field(
        None,
        description="Number of leaflets (e.g., 2 or 3)."
    )
    AV_stenosis_severity: Optional[StenosisSeverity] = Field(
        None,
        description="Aortic valve (or neo-aortic valve if aortic valve not available) stenosis presence/severity."
    )
    AV_regurgitation_severity: Optional[RegurgitationSeverity] = Field(
        None,
        description="Aortic regurgitation (or neo-aortic valve if aortic valve not available) presence/severity."
    )
    AV_peak_pressure_gradient: Optional[NumericValue] = Field(
        None,
        description="Peak measured pressure gradient across the aortic valve (or neo-aortic valve if aortic valve not available)."
    )
    AV_mean_pressure_gradient: Optional[NumericValue] = Field(
        None,
        description="Mean measured pressure gradient across the aortic valve (or neo-aortic valve if aortic valve not available)."
    )
    LVOT_obstruction: Optional[bool] = Field(
        None,
        description="True if there is any LVOT obstruction."
    )
    LVOT_obstruction_dynamic: Optional[str] = Field(
        None,
        description="If LVOT_obstruction 'True': specify if dynamic, fixed, or dynamic and fixed obstruction."
    )
     

class Valves(BaseModel):
    """Top-level container for all valves."""
    tricuspid: Optional[TricuspidValve] = None
    pulmonary: Optional[PulmonaryValve] = None
    mitral: Optional[MitralValve] = None
    aortic: Optional[AorticValve] = None


# Great Vessels

class Aorta(BaseModel):
    """Aorta details."""
    arch_sidedness: Optional[Sidedness] = Field(
        None,
        description="For example, Left arch or Right arch."
    )
    aortic_root_size: Optional[NumericValue] = Field(
        None,
        description="Aortic root dimension (in systole if both systole and diastole are available)."
    )
    ascending_aorta_diameter: Optional[NumericValue] = Field(
        None,
        description="Ascending aorta diameter (in systole if both systole and diastole are available)."
    )
    aortic_isthmus_size: Optional[NumericValue] = Field(
        None,
        description="Aortic isthmus dimension (in systole if both systole and diastole are available)."
    )
    coarctation: Optional[bool] = Field(
        None,
        description="True if there is any aortic coarctation."
    )
    coarctation_gradient: Optional[NumericValue] = Field(
        None,
        description="Peak pressure gradient across the coarctation, if present."
    )

class PulmonaryArtery(BaseModel):
    """Pulmonary artery details."""
    main_pa_dilation: Optional[DilationSeverity] = Field(
        None, 
        description="Describe the degree of main pulmonary artery (MPA) dilation as commented on in the report."
    )
    mpa_size: Optional[NumericValue] = Field(
        None,
        description="Main pulmonary artery (MPA) diameter."
    )
    mpa_stenosis: Optional[bool] = Field(
        None,
        description="True if there is any main pulmonary artery (MPA) stenosis."
    )
    mpa_flow_reversal: Optional[bool] = Field(
        None,
        description="True if there is any main pulmonary artery (MPA) flow reversal."
    )
    mpa_gradient: Optional[NumericValue] = Field(
        None,
        description="Peak gradient in main pulmonary artery (MPA)."
    )
    right_pa_dilation: Optional[DilationSeverity] = Field(
        None, 
        description="Describe the degree of right pulmonary artery (RPA) dilation as commented on in the report."
    )
    rpa_size: Optional[NumericValue] = Field(
        None,
        description="Right pulmonary artery (RPA) diameter."
    )
    rpa_stenosis: Optional[bool] = Field(
        None,
        description="True if there is any right pulmonary artery (RPA) stenosis."
    )
    rpa_flow_reversal: Optional[bool] = Field(
        None,
        description="True if there is any right pulmonary artery (RPA) flow reversal."
    )
    rpa_gradient: Optional[NumericValue] = Field(
        None,
        description="Peak gradient in right pulmonary artery (RPA)."
    )
    left: Optional[DilationSeverity] = Field(
        None, 
        description="Describe the degree of left pulmonary artery (LPA) dilation as commented on in the report."
    )
    lpa_size: Optional[NumericValue] = Field(
        None,
        description="Left pulmonary artery (LPA) diameter."
    )
    lpa_stenosis: Optional[bool] = Field(
        None,
        description="True if there is any left pulmonary artery (LPA) stenosis."
    )
    lpa_flow_reversal: Optional[bool] = Field(
        None,
        description="True if there is any left pulmonary artery (LPA) flow reversal."
    )
    lpa_gradient: Optional[NumericValue] = Field(
        None,
        description="Peak gradient in left pulmonary artery (LPA)."
    )

class PulmonaryVeins(BaseModel):
    """Pulmonary vein details."""
    pv_visualized: Optional[float] = Field(
        None,
        description="Total number of pulmonary veins visualized for this patient, either in the current study or by prior evaluation. This may not exceed 4."
    )
    pv_normal: Optional[bool] = Field(
        None,
        description="True if all of the pulmonary veins drain normally to the left atrium."
    )
    pv_anomalous: Optional[bool] = Field(
        None,
        description="True if there is anomalous pulmonary venous drainage."
    )
    pv_anomalous_type: Optional[str] = Field(
        None,
        description="If 'True' in pv_anomalous: mention type of anomaly (i.e. TAPVR or PAPVR)."
    ) 
    pv_stenosis: Optional[bool] = Field(
        None,
        description="True if there is stenosis or obstruction of any of the pulmonary venous drainage."
    )
    pv_stenosis_type: Optional[str] = Field(
        None,
        description="If 'True' in pv_stenosis: describe which vein(s) appear obstructed."
    )
    
class GreatVessels(BaseModel):
    """Container for great vessel details."""
    aorta: Optional[Aorta] = None
    pulmonary_artery: Optional[PulmonaryArtery] = None
    pulmonary_veins:  Optional[PulmonaryVeins] = None

# Pulmonary Hypertension

class PulmonaryHypertension(BaseModel):
    """Pulmonary hypertension assessment."""
    severity: Optional[str] = Field(
        None,
        description="None, mild, moderate, severe, half-systemic, etc."
    )
    TR_jet_gradient: Optional[NumericValue] = Field(
        None,
        description="Tricuspid regurgitation jet gradient (mmHg)."
    )
    IVS_flattening_in_systole: Optional[bool] = Field(
        None,
        description="True if interventricular septal flattening, bowing, or bulging occurs in systole."
    )


# Atrial communication

class ASD(BaseModel):
    """Atrial communication (ASD/PFO) details currently present."""
    atrial_communication_present: Optional[bool] = Field(
        None,
        description="True if a current ASD is present at time of this study."
    )
    asd_types: Optional[List[ASD_type]] = Field(
        None,
        description="If 'True' in atrial_communication_present: mention anatomy of atrial communication types if multiple are present at time of this study."
    )
    asd_type_other: Optional[str] = Field(
        None,
        description="If 'Other' was selected in ASD_type, specify here."
    )
    asd_size: Optional[Size] = Field(
        None, 
        description="Size of the atrial communication (e.g., largest one if multiple) present at time of this study."
    )
    asd_direction_of_flow: Optional[Direction] = Field(
        None, 
        description="Direction of shunting across the atrial communication."
    )


# Ventricular communication

class VSD(BaseModel):
    """Ventricular septal defect (VSD) details currently present."""
    ventricular_communication_present: Optional[bool] = Field(
        None,
        description="True if a current VSD is present at time of this study."
    )
    vsd_types: Optional[List[VSD_type]] = Field(
        None,
        description="If 'True' in ventricular_communication_present: mention anatomy of ventricular communication types if multiple are present at time of this study."
    )
    vsd_type_other: Optional[str] = Field(
        None,
        description="If 'Other' was selected in VSD_type, specify here."
    )
    vsd_size: Optional[Size] = Field(
        None, 
        description="Size of the VSD (largest if multiple) present at time of this study."
    )
    vsd_direction_of_flow: Optional[Direction] = Field(
        None, 
        description="Direction of shunting across the VSD."
    )
    vsd_peak_gradient: Optional[NumericValue] = Field(
        None,
        description="Peak pressure gradient across the VSD."
    )


# PDA

class PDA(BaseModel):
    """Patent ductus arteriosus details."""
    present: Optional[bool] = Field(
        None,
        description="True if a PDA is currently present."
    )
    direction_of_flow: Optional[Direction] = Field(
        None,
        description="Direction of shunting across the PDA."
    )
    size: Optional[NumericValue] = Field(
        None, 
        description="Patent ductus arteriosus size."
    )
    peak_gradient: Optional[NumericValue] = Field(
        None,
        description="Peak pressure gradient across the PDA."
    )


# Coronary arteries

class CA(BaseModel):
    LCA_structure: Optional[LCA] = Field(
        None,
        description="Describe the left coronary artery anatomy. Select other if the left coronary anatomy does not conform to one of the options."
    )
    LCA_other: Optional[str] = Field(
        None,
        description="If 'Other' was selected in LCA_structure, specify here."
    )
    RCA_structure: Optional[RCA] = Field(
        None,
        description="Describe the right coronary artery anatomy. Select other if the right coronary anatomy does not conform to one of the options."
    )
    RCA_other: Optional[str] = Field(
        None,
        description="If 'Other' was selected in RCA_structure, specify here."
    )
    CA_anomaly: Optional[CA_abnormality] = Field(
        None,
        description="Describe any additional coronary artery anomaly not aforementioned in LCA_structure, LCA_other, RCA_structure, or RCA_other."
    )



# Caval Veins

class SVC(BaseModel):
    """SVC anatomy."""
    RSVC_present: Optional[RSVC] = Field(
        None,
        description="Describe prescence of a right superior vena cava."
    )
    LSVC_present: Optional[LSVC] = Field(
        None,
        description="Describe prescence of a left superior vena cava."
    )
    RSVC_stenosis: Optional[bool] = Field(
        None,
        description="True if there is right superior vena caval stenosis."
    )
    LSVC_stenosis: Optional[bool] = Field(
        None,
        description="True if there is left superior vena caval stenosis."
    )
    Bilateral_SVC: Optional[bool] = Field(
        None, 
        description="True if there are bilateral superior vena cavae."
    )
    Bridging_vein: Optional[bool] = Field(
        None, 
        description="True if a bridging vein is present."
    )
    
class IVC(BaseModel):
    """IVC anatomy."""
    IVC_anatomy: Optional[IVC_option] = Field(
        None,
        description="Describe IVC anatomy as normal, interrupted, or stenotic."
    ) 
    IVC_other: Optional[str] = Field(
        None,
        description="If 'Other' was selected in IVC_anatomy, specify here."
    )

class Fontan(BaseModel):
    """Fontan."""
    fontan_present: Optional[bool] = Field(
        None,
        description="True if a Fontan circulation is present currently."
    ) 
    fontan_type: Optional[str] = Field(
        None,
        description="If 'True' in fontan_present: describe what type of Fontan (lateral tunnel fontan, extracardiac fontan, classic fontan."
    ) 
    fontan_fenestration: Optional[bool] = Field(
        None,
        description="True if a Fontan fenestration is present currently"
    ) 
    fontan_gradient: Optional[float] = Field(
        None,
        description="Gradient across the Fontan fenestraion if 'True' in fontan_present."
    ) 

# Surgical / Device History / Other

class SurgicalHistory(BaseModel):
    """Surgical or interventional history."""
    prior_surgical_interventions: Optional[List[SurgicalIntervention]] = Field(
        None, 
        description="Details of previous surgeries or repairs. Include the date of the surgery, procedure, or repair for each one if present."
    )
    EP_devices: Optional[list] = Field(
        None,
        description="List any and all electrophysiology devices currently implanted (pacemaker, ICD, leadless pacemaker, epicardial pacemaker)"
    )
    VAD_devices: Optional[list] = Field(
        None,
        description="List any and all advanced heart failure devices currently implanted (ECMO, Heartmate, Berlin VAD, Impella, Balloon pump)"
    )
    Mass: Optional[str] = Field(
        None,
        description="List any and all masses present (lipoma, vegetation, cyst, tumor, abscess)"
    )


class DiagnosisHistory(BaseModel):
    """Prior or current cardiac diagnoses."""
    cardiac_diagnoses: Optional[List[DiagnosisItem]] = Field(
        None,
        description="List of prior and current cardiac diagnoses with their respective dates, status, and source references."
    )
    genetic_or_metabolic_disorders: Optional[List[DiagnosisItem]] = Field(
        None,
        description="List of known genetic, metabolic, or systemic disorders associated with cardiac disease, including date, status, and source reference (e.g., Trisomy 21, Fabry disease)."
    )
        
class Effusion(BaseModel):
    pericardial_effusion: Optional[bool] = Field(
        None,
        description="True if pericardial effusion present."
    )
    pericardial_effusion_size: Optional[Size] = Field(
        None, 
        description="If 'True' pericardial_effusion: describe the size of the pericardial effusion."
    )
    right_pleural_effusion: Optional[bool] = Field(
        None,
        description="True if a right pleural effusion is present."
    )
    right_pleural_effusion_size: Optional[Size] = Field(
        None, 
        description="If 'True' right_pleural_effusion: describe the size of the right pleural effusion."
    )
    left_pleural_effusion: Optional[bool] = Field(
        None,
        description="True if a left pleural effusion is present."
    )
    left_pleural_effusion_size: Optional[Size] = Field(
        None, 
        description="If 'True' left_pleural_effusion: describe the size of the left pleural effusion."
    )

# Patient Info

class PatientInfo(BaseModel):
    mrn: Optional[str] = Field(None, description="Medical Record Number")
    name: Optional[str] = Field(None, description="Full patient name")
    blood_pressure: Optional[str] = Field(None, description="Blood pressure, format: systolic/diastolic mmHg")
    height_cm: Optional[float] = Field(None, description="Height in centimeters")
    weight_kg: Optional[float] = Field(None, description="Weight in kilograms")
    bsa_m2: Optional[float] = Field(None, description="Body surface area in square meters")
    
#
# 4) TOP-LEVEL ECHO REPORT MODEL
#

class EchoReport(BaseModel):
    """Main Pydantic model capturing the full echo report."""

    patient_info: Optional[PatientInfo] = None
    situs: Optional[Situs] = None
    cardiac_position: Optional[CardiacPosition] = None
    atria: Optional[Atria] = None
    ventricles: Optional[Ventricles] = None
    valves: Optional[Valves] = None
    great_vessels: Optional[GreatVessels] = None
    pHTN: Optional[PulmonaryHypertension] = None

    # Shunts / Additional findings
    asd: Optional[ASD] = None
    vsd: Optional[VSD] = None
    pda: Optional[PDA] = None
    coronaries: Optional[CA] = None
    svc: Optional[SVC] = None
    ivc: Optional[IVC] = None
    fontan: Optional[Fontan] = None

    # Additional structural/surgical/device data
    surgical_history: Optional[SurgicalHistory] = None
    diagnoses: Optional[DiagnosisHistory] = None
    effusion: Optional[Effusion] = None

    class Config:
        # If you prefer enum field values as strings in the JSON output:
        use_enum_values = True

