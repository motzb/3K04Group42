/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: AOO.c
 *
 * Code generated for Simulink model 'AOO'.
 *
 * Model version                  : 1.11
 * Simulink Coder version         : 9.7 (R2022a) 13-Nov-2021
 * C/C++ source code generated on : Mon Oct  3 16:29:12 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "AOO.h"
#include "rtwtypes.h"
#include <math.h>
#include "AOO_types.h"

/* Named constants for Chart: '<Root>/Chart' */
#define AOO_IN_Charging_Discharging    ((uint8_T)1U)
#define AOO_IN_Pace_Heart              ((uint8_T)2U)

/* Block signals (default storage) */
B_AOO_T AOO_B;

/* Block states (default storage) */
DW_AOO_T AOO_DW;

/* Real-time model */
static RT_MODEL_AOO_T AOO_M_;
RT_MODEL_AOO_T *const AOO_M = &AOO_M_;

/* Model step function */
void AOO_step(void)
{
  boolean_T rtb_ATR_GND_CTRL;
  boolean_T rtb_ATR_PACE_CTRL;
  boolean_T rtb_PACE_CHARGE_CTRL;

  /* Chart: '<Root>/Chart' incorporates:
   *  Constant: '<Root>/p_aPaceWidth'
   *  Constant: '<Root>/p_lowrateinterval'
   */
  if (AOO_DW.temporalCounter_i1 < MAX_uint32_T) {
    AOO_DW.temporalCounter_i1++;
  }

  if (AOO_DW.is_active_c1_AOO == 0U) {
    AOO_DW.is_active_c1_AOO = 1U;
    AOO_DW.is_c1_AOO = AOO_IN_Charging_Discharging;
    AOO_DW.temporalCounter_i1 = 0U;
    rtb_ATR_PACE_CTRL = false;
    rtb_PACE_CHARGE_CTRL = true;
    rtb_ATR_GND_CTRL = true;
    AOO_B.Z_ATR_CTRL = false;
  } else if (AOO_DW.is_c1_AOO == AOO_IN_Charging_Discharging) {
    rtb_ATR_PACE_CTRL = false;
    rtb_PACE_CHARGE_CTRL = true;
    rtb_ATR_GND_CTRL = true;
    AOO_B.Z_ATR_CTRL = false;
    if (AOO_DW.temporalCounter_i1 >= (uint32_T)ceil(1.0 /
         AOO_P.p_lowrateinterval_Value * 60000.0 - AOO_P.p_aPaceWidth_Value)) {
      AOO_DW.is_c1_AOO = AOO_IN_Pace_Heart;
      AOO_DW.temporalCounter_i1 = 0U;
      rtb_ATR_PACE_CTRL = true;
      rtb_PACE_CHARGE_CTRL = false;
      rtb_ATR_GND_CTRL = false;
    }
  } else {
    /* case IN_Pace_Heart: */
    rtb_ATR_PACE_CTRL = true;
    rtb_PACE_CHARGE_CTRL = false;
    rtb_ATR_GND_CTRL = false;
    if (AOO_DW.temporalCounter_i1 >= (uint32_T)ceil(AOO_P.p_aPaceWidth_Value)) {
      AOO_DW.is_c1_AOO = AOO_IN_Charging_Discharging;
      AOO_DW.temporalCounter_i1 = 0U;
      rtb_ATR_PACE_CTRL = false;
      rtb_PACE_CHARGE_CTRL = true;
      rtb_ATR_GND_CTRL = true;
      AOO_B.Z_ATR_CTRL = false;
    }
  }

  /* End of Chart: '<Root>/Chart' */

  /* MATLABSystem: '<Root>/ATR_GND CTRL' */
  MW_digitalIO_write(AOO_DW.obj_e.MW_DIGITALIO_HANDLE, rtb_ATR_GND_CTRL);

  /* MATLABSystem: '<Root>/ATR_PACE_CTRL' */
  MW_digitalIO_write(AOO_DW.obj_l.MW_DIGITALIO_HANDLE, rtb_ATR_PACE_CTRL);

  /* MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
  MW_digitalIO_write(AOO_DW.obj_n.MW_DIGITALIO_HANDLE, rtb_PACE_CHARGE_CTRL);

  /* MATLABSystem: '<Root>/PACE_GND_CTRL' */
  MW_digitalIO_write(AOO_DW.obj_k.MW_DIGITALIO_HANDLE, true);

  /* MATLABSystem: '<Root>/Z_ATR_CTRL' */
  MW_digitalIO_write(AOO_DW.obj.MW_DIGITALIO_HANDLE, AOO_B.Z_ATR_CTRL);

  /* MATLABSystem: '<Root>/PACING_REF_PWM' incorporates:
   *  Constant: '<Root>/p_aPaceAmp'
   */
  MW_PWM_SetDutyCycle(AOO_DW.obj_j.MW_PWM_HANDLE, AOO_P.p_aPaceAmp_Value);
}

/* Model initialize function */
void AOO_initialize(void)
{
  {
    freedomk64f_DigitalWrite_AOO_T *obj;
    freedomk64f_PWMOutput_AOO_T *obj_0;

    /* Start for MATLABSystem: '<Root>/ATR_GND CTRL' */
    AOO_DW.obj_e.matlabCodegenIsDeleted = true;
    AOO_DW.obj_e.isInitialized = 0;
    AOO_DW.obj_e.matlabCodegenIsDeleted = false;
    obj = &AOO_DW.obj_e;
    AOO_DW.obj_e.isSetupComplete = false;
    AOO_DW.obj_e.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(11U, 1);
    AOO_DW.obj_e.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/ATR_PACE_CTRL' */
    AOO_DW.obj_l.matlabCodegenIsDeleted = true;
    AOO_DW.obj_l.isInitialized = 0;
    AOO_DW.obj_l.matlabCodegenIsDeleted = false;
    obj = &AOO_DW.obj_l;
    AOO_DW.obj_l.isSetupComplete = false;
    AOO_DW.obj_l.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(8U, 1);
    AOO_DW.obj_l.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
    AOO_DW.obj_n.matlabCodegenIsDeleted = true;
    AOO_DW.obj_n.isInitialized = 0;
    AOO_DW.obj_n.matlabCodegenIsDeleted = false;
    obj = &AOO_DW.obj_n;
    AOO_DW.obj_n.isSetupComplete = false;
    AOO_DW.obj_n.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(2U, 1);
    AOO_DW.obj_n.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACE_GND_CTRL' */
    AOO_DW.obj_k.matlabCodegenIsDeleted = true;
    AOO_DW.obj_k.isInitialized = 0;
    AOO_DW.obj_k.matlabCodegenIsDeleted = false;
    obj = &AOO_DW.obj_k;
    AOO_DW.obj_k.isSetupComplete = false;
    AOO_DW.obj_k.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(10U, 1);
    AOO_DW.obj_k.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Z_ATR_CTRL' */
    AOO_DW.obj.matlabCodegenIsDeleted = true;
    AOO_DW.obj.isInitialized = 0;
    AOO_DW.obj.matlabCodegenIsDeleted = false;
    obj = &AOO_DW.obj;
    AOO_DW.obj.isSetupComplete = false;
    AOO_DW.obj.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(4U, 1);
    AOO_DW.obj.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACING_REF_PWM' */
    AOO_DW.obj_j.matlabCodegenIsDeleted = true;
    AOO_DW.obj_j.isInitialized = 0;
    AOO_DW.obj_j.matlabCodegenIsDeleted = false;
    obj_0 = &AOO_DW.obj_j;
    AOO_DW.obj_j.isSetupComplete = false;
    AOO_DW.obj_j.isInitialized = 1;
    obj_0->MW_PWM_HANDLE = MW_PWM_Open(5U, 2000.0, 0.0);
    MW_PWM_Start(AOO_DW.obj_j.MW_PWM_HANDLE);
    AOO_DW.obj_j.isSetupComplete = true;
  }
}

/* Model terminate function */
void AOO_terminate(void)
{
  /* Terminate for MATLABSystem: '<Root>/ATR_GND CTRL' */
  if (!AOO_DW.obj_e.matlabCodegenIsDeleted) {
    AOO_DW.obj_e.matlabCodegenIsDeleted = true;
    if ((AOO_DW.obj_e.isInitialized == 1) && AOO_DW.obj_e.isSetupComplete) {
      MW_digitalIO_close(AOO_DW.obj_e.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/ATR_GND CTRL' */

  /* Terminate for MATLABSystem: '<Root>/ATR_PACE_CTRL' */
  if (!AOO_DW.obj_l.matlabCodegenIsDeleted) {
    AOO_DW.obj_l.matlabCodegenIsDeleted = true;
    if ((AOO_DW.obj_l.isInitialized == 1) && AOO_DW.obj_l.isSetupComplete) {
      MW_digitalIO_close(AOO_DW.obj_l.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/ATR_PACE_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
  if (!AOO_DW.obj_n.matlabCodegenIsDeleted) {
    AOO_DW.obj_n.matlabCodegenIsDeleted = true;
    if ((AOO_DW.obj_n.isInitialized == 1) && AOO_DW.obj_n.isSetupComplete) {
      MW_digitalIO_close(AOO_DW.obj_n.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/PACE_GND_CTRL' */
  if (!AOO_DW.obj_k.matlabCodegenIsDeleted) {
    AOO_DW.obj_k.matlabCodegenIsDeleted = true;
    if ((AOO_DW.obj_k.isInitialized == 1) && AOO_DW.obj_k.isSetupComplete) {
      MW_digitalIO_close(AOO_DW.obj_k.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACE_GND_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/Z_ATR_CTRL' */
  if (!AOO_DW.obj.matlabCodegenIsDeleted) {
    AOO_DW.obj.matlabCodegenIsDeleted = true;
    if ((AOO_DW.obj.isInitialized == 1) && AOO_DW.obj.isSetupComplete) {
      MW_digitalIO_close(AOO_DW.obj.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Z_ATR_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/PACING_REF_PWM' */
  if (!AOO_DW.obj_j.matlabCodegenIsDeleted) {
    AOO_DW.obj_j.matlabCodegenIsDeleted = true;
    if ((AOO_DW.obj_j.isInitialized == 1) && AOO_DW.obj_j.isSetupComplete) {
      MW_PWM_Stop(AOO_DW.obj_j.MW_PWM_HANDLE);
      MW_PWM_Close(AOO_DW.obj_j.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACING_REF_PWM' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
