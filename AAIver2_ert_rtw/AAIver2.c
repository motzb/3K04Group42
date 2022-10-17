/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: AAIver2.c
 *
 * Code generated for Simulink model 'AAIver2'.
 *
 * Model version                  : 1.12
 * Simulink Coder version         : 9.7 (R2022a) 13-Nov-2021
 * C/C++ source code generated on : Mon Oct 17 17:06:27 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "AAIver2.h"
#include "rtwtypes.h"
#include <math.h>
#include "AAIver2_types.h"

/* Named constants for Chart: '<S1>/Chart1' */
#define AAIver2_IN_Charging_Discharging ((uint8_T)1U)
#define AAIver2_IN_Pace_Heart          ((uint8_T)2U)
#define AAIver2_IN_Pulse_Sensed        ((uint8_T)3U)

/* Block signals (default storage) */
B_AAIver2_T AAIver2_B;

/* Block states (default storage) */
DW_AAIver2_T AAIver2_DW;

/* Real-time model */
static RT_MODEL_AAIver2_T AAIver2_M_;
RT_MODEL_AAIver2_T *const AAIver2_M = &AAIver2_M_;

/* Model step function */
void AAIver2_step(void)
{
  boolean_T rtb_ATR_CMP_DETECT_0;

  /* MATLABSystem: '<Root>/ATR_CMP_DETECT' */
  if (AAIver2_DW.obj.SampleTime != AAIver2_P.ATR_CMP_DETECT_SampleTime) {
    AAIver2_DW.obj.SampleTime = AAIver2_P.ATR_CMP_DETECT_SampleTime;
  }

  rtb_ATR_CMP_DETECT_0 = MW_digitalIO_read(AAIver2_DW.obj.MW_DIGITALIO_HANDLE);

  /* Chart: '<S1>/cycle_time_calc' incorporates:
   *  Constant: '<Root>/p_aPaceWidth'
   *  Constant: '<Root>/p_lowrateinterval'
   */
  if (AAIver2_DW.is_active_c1_AAIver2 == 0U) {
    AAIver2_DW.is_active_c1_AAIver2 = 1U;
    AAIver2_B.cycle_time = 1.0 / AAIver2_P.p_lowrateinterval_Value * 60000.0 -
      AAIver2_P.p_aPaceWidth_Value;
  }

  /* End of Chart: '<S1>/cycle_time_calc' */

  /* Chart: '<S1>/Chart1' incorporates:
   *  Constant: '<Root>/p_ARP'
   *  Constant: '<Root>/p_aPaceWidth'
   *  MATLABSystem: '<Root>/ATR_CMP_DETECT'
   */
  if (AAIver2_DW.temporalCounter_i1 < MAX_uint32_T) {
    AAIver2_DW.temporalCounter_i1++;
  }

  if (AAIver2_DW.is_active_c4_AAIver2 == 0U) {
    AAIver2_DW.is_active_c4_AAIver2 = 1U;
    AAIver2_DW.is_c4_AAIver2 = AAIver2_IN_Charging_Discharging;
    AAIver2_DW.temporalCounter_i1 = 0U;
    AAIver2_B.ATR_PACE_CTRL = false;
    AAIver2_B.VENT_PACE_CTRL = false;
    AAIver2_B.PACE_CHARGE_CTRL = true;
    AAIver2_B.ATR_GND_CTRL = true;
    AAIver2_B.PACE_GND_CTRL = true;
    AAIver2_B.Z_ATR_CTRL = false;
    AAIver2_B.FRONTEND_CTRL = true;
  } else {
    switch (AAIver2_DW.is_c4_AAIver2) {
     case AAIver2_IN_Charging_Discharging:
      AAIver2_B.ATR_PACE_CTRL = false;
      AAIver2_B.VENT_PACE_CTRL = false;
      AAIver2_B.PACE_CHARGE_CTRL = true;
      AAIver2_B.ATR_GND_CTRL = true;
      AAIver2_B.PACE_GND_CTRL = true;
      AAIver2_B.Z_ATR_CTRL = false;
      AAIver2_B.FRONTEND_CTRL = true;
      if (AAIver2_DW.temporalCounter_i1 >= (uint32_T)ceil(AAIver2_B.cycle_time))
      {
        AAIver2_DW.is_c4_AAIver2 = AAIver2_IN_Pace_Heart;
        AAIver2_DW.temporalCounter_i1 = 0U;
        AAIver2_B.ATR_PACE_CTRL = true;
        AAIver2_B.PACE_CHARGE_CTRL = false;
        AAIver2_B.ATR_GND_CTRL = false;
      } else if (rtb_ATR_CMP_DETECT_0) {
        AAIver2_DW.is_c4_AAIver2 = AAIver2_IN_Pulse_Sensed;
        AAIver2_DW.temporalCounter_i1 = 0U;
      }
      break;

     case AAIver2_IN_Pace_Heart:
      AAIver2_B.ATR_PACE_CTRL = true;
      AAIver2_B.PACE_CHARGE_CTRL = false;
      AAIver2_B.PACE_GND_CTRL = true;
      AAIver2_B.ATR_GND_CTRL = false;
      if (AAIver2_DW.temporalCounter_i1 >= (uint32_T)ceil
          (AAIver2_P.p_aPaceWidth_Value)) {
        AAIver2_DW.is_c4_AAIver2 = AAIver2_IN_Charging_Discharging;
        AAIver2_DW.temporalCounter_i1 = 0U;
        AAIver2_B.ATR_PACE_CTRL = false;
        AAIver2_B.VENT_PACE_CTRL = false;
        AAIver2_B.PACE_CHARGE_CTRL = true;
        AAIver2_B.ATR_GND_CTRL = true;
        AAIver2_B.Z_ATR_CTRL = false;
        AAIver2_B.FRONTEND_CTRL = true;
      }
      break;

     default:
      /* case IN_Pulse_Sensed: */
      if (AAIver2_DW.temporalCounter_i1 >= (uint32_T)ceil(AAIver2_P.p_ARP_Value))
      {
        AAIver2_DW.is_c4_AAIver2 = AAIver2_IN_Charging_Discharging;
        AAIver2_DW.temporalCounter_i1 = 0U;
        AAIver2_B.ATR_PACE_CTRL = false;
        AAIver2_B.VENT_PACE_CTRL = false;
        AAIver2_B.PACE_CHARGE_CTRL = true;
        AAIver2_B.ATR_GND_CTRL = true;
        AAIver2_B.PACE_GND_CTRL = true;
        AAIver2_B.Z_ATR_CTRL = false;
        AAIver2_B.FRONTEND_CTRL = true;
      }
      break;
    }
  }

  /* End of Chart: '<S1>/Chart1' */

  /* MATLABSystem: '<Root>/ATR_GND CTRL' */
  MW_digitalIO_write(AAIver2_DW.obj_e.MW_DIGITALIO_HANDLE,
                     AAIver2_B.ATR_GND_CTRL);

  /* MATLABSystem: '<Root>/ATR_PACE_CTRL' */
  MW_digitalIO_write(AAIver2_DW.obj_n.MW_DIGITALIO_HANDLE,
                     AAIver2_B.ATR_PACE_CTRL);

  /* MATLABSystem: '<Root>/FRONTEND_CTRL' */
  MW_digitalIO_write(AAIver2_DW.obj_j.MW_DIGITALIO_HANDLE,
                     AAIver2_B.FRONTEND_CTRL);

  /* MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
  MW_digitalIO_write(AAIver2_DW.obj_lf.MW_DIGITALIO_HANDLE,
                     AAIver2_B.PACE_CHARGE_CTRL);

  /* MATLABSystem: '<Root>/PACE_GND_CTRL' */
  MW_digitalIO_write(AAIver2_DW.obj_h0.MW_DIGITALIO_HANDLE,
                     AAIver2_B.PACE_GND_CTRL);

  /* MATLABSystem: '<Root>/VENT_PACE_CTRL' */
  MW_digitalIO_write(AAIver2_DW.obj_h.MW_DIGITALIO_HANDLE,
                     AAIver2_B.VENT_PACE_CTRL);

  /* MATLABSystem: '<Root>/Z_ATR_CTRL' */
  MW_digitalIO_write(AAIver2_DW.obj_g.MW_DIGITALIO_HANDLE, AAIver2_B.Z_ATR_CTRL);

  /* MATLABSystem: '<Root>/ATR_CMP_REF_PWM Output' incorporates:
   *  Constant: '<Root>/ATR_CMP_REF_PWM'
   */
  MW_PWM_SetDutyCycle(AAIver2_DW.obj_l.MW_PWM_HANDLE,
                      AAIver2_P.ATR_CMP_REF_PWM_Value);

  /* MATLABSystem: '<Root>/PACING_REF_PWM Output' incorporates:
   *  Constant: '<Root>/PACING_REF_PWM'
   */
  MW_PWM_SetDutyCycle(AAIver2_DW.obj_o.MW_PWM_HANDLE,
                      AAIver2_P.PACING_REF_PWM_Value);
}

/* Model initialize function */
void AAIver2_initialize(void)
{
  {
    freedomk64f_DigitalRead_AAIve_T *obj;
    freedomk64f_DigitalWrite_AAIv_T *obj_0;
    freedomk64f_PWMOutput_AAIver2_T *obj_1;

    /* Start for MATLABSystem: '<Root>/ATR_CMP_DETECT' */
    AAIver2_DW.obj.matlabCodegenIsDeleted = true;
    AAIver2_DW.obj.isInitialized = 0;
    AAIver2_DW.obj.SampleTime = -1.0;
    AAIver2_DW.obj.matlabCodegenIsDeleted = false;
    AAIver2_DW.obj.SampleTime = AAIver2_P.ATR_CMP_DETECT_SampleTime;
    obj = &AAIver2_DW.obj;
    AAIver2_DW.obj.isSetupComplete = false;
    AAIver2_DW.obj.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(0U, 0);
    AAIver2_DW.obj.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/ATR_GND CTRL' */
    AAIver2_DW.obj_e.matlabCodegenIsDeleted = true;
    AAIver2_DW.obj_e.isInitialized = 0;
    AAIver2_DW.obj_e.matlabCodegenIsDeleted = false;
    obj_0 = &AAIver2_DW.obj_e;
    AAIver2_DW.obj_e.isSetupComplete = false;
    AAIver2_DW.obj_e.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(11U, 1);
    AAIver2_DW.obj_e.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/ATR_PACE_CTRL' */
    AAIver2_DW.obj_n.matlabCodegenIsDeleted = true;
    AAIver2_DW.obj_n.isInitialized = 0;
    AAIver2_DW.obj_n.matlabCodegenIsDeleted = false;
    obj_0 = &AAIver2_DW.obj_n;
    AAIver2_DW.obj_n.isSetupComplete = false;
    AAIver2_DW.obj_n.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(8U, 1);
    AAIver2_DW.obj_n.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/FRONTEND_CTRL' */
    AAIver2_DW.obj_j.matlabCodegenIsDeleted = true;
    AAIver2_DW.obj_j.isInitialized = 0;
    AAIver2_DW.obj_j.matlabCodegenIsDeleted = false;
    obj_0 = &AAIver2_DW.obj_j;
    AAIver2_DW.obj_j.isSetupComplete = false;
    AAIver2_DW.obj_j.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(13U, 1);
    AAIver2_DW.obj_j.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
    AAIver2_DW.obj_lf.matlabCodegenIsDeleted = true;
    AAIver2_DW.obj_lf.isInitialized = 0;
    AAIver2_DW.obj_lf.matlabCodegenIsDeleted = false;
    obj_0 = &AAIver2_DW.obj_lf;
    AAIver2_DW.obj_lf.isSetupComplete = false;
    AAIver2_DW.obj_lf.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(2U, 1);
    AAIver2_DW.obj_lf.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACE_GND_CTRL' */
    AAIver2_DW.obj_h0.matlabCodegenIsDeleted = true;
    AAIver2_DW.obj_h0.isInitialized = 0;
    AAIver2_DW.obj_h0.matlabCodegenIsDeleted = false;
    obj_0 = &AAIver2_DW.obj_h0;
    AAIver2_DW.obj_h0.isSetupComplete = false;
    AAIver2_DW.obj_h0.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(10U, 1);
    AAIver2_DW.obj_h0.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/VENT_PACE_CTRL' */
    AAIver2_DW.obj_h.matlabCodegenIsDeleted = true;
    AAIver2_DW.obj_h.isInitialized = 0;
    AAIver2_DW.obj_h.matlabCodegenIsDeleted = false;
    obj_0 = &AAIver2_DW.obj_h;
    AAIver2_DW.obj_h.isSetupComplete = false;
    AAIver2_DW.obj_h.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(9U, 1);
    AAIver2_DW.obj_h.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Z_ATR_CTRL' */
    AAIver2_DW.obj_g.matlabCodegenIsDeleted = true;
    AAIver2_DW.obj_g.isInitialized = 0;
    AAIver2_DW.obj_g.matlabCodegenIsDeleted = false;
    obj_0 = &AAIver2_DW.obj_g;
    AAIver2_DW.obj_g.isSetupComplete = false;
    AAIver2_DW.obj_g.isInitialized = 1;
    obj_0->MW_DIGITALIO_HANDLE = MW_digitalIO_open(4U, 1);
    AAIver2_DW.obj_g.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/ATR_CMP_REF_PWM Output' */
    AAIver2_DW.obj_l.matlabCodegenIsDeleted = true;
    AAIver2_DW.obj_l.isInitialized = 0;
    AAIver2_DW.obj_l.matlabCodegenIsDeleted = false;
    obj_1 = &AAIver2_DW.obj_l;
    AAIver2_DW.obj_l.isSetupComplete = false;
    AAIver2_DW.obj_l.isInitialized = 1;
    obj_1->MW_PWM_HANDLE = MW_PWM_Open(6U, 2000.0, 0.0);
    MW_PWM_Start(AAIver2_DW.obj_l.MW_PWM_HANDLE);
    AAIver2_DW.obj_l.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PACING_REF_PWM Output' */
    AAIver2_DW.obj_o.matlabCodegenIsDeleted = true;
    AAIver2_DW.obj_o.isInitialized = 0;
    AAIver2_DW.obj_o.matlabCodegenIsDeleted = false;
    obj_1 = &AAIver2_DW.obj_o;
    AAIver2_DW.obj_o.isSetupComplete = false;
    AAIver2_DW.obj_o.isInitialized = 1;
    obj_1->MW_PWM_HANDLE = MW_PWM_Open(5U, 2000.0, 0.0);
    MW_PWM_Start(AAIver2_DW.obj_o.MW_PWM_HANDLE);
    AAIver2_DW.obj_o.isSetupComplete = true;
  }
}

/* Model terminate function */
void AAIver2_terminate(void)
{
  /* Terminate for MATLABSystem: '<Root>/ATR_CMP_DETECT' */
  if (!AAIver2_DW.obj.matlabCodegenIsDeleted) {
    AAIver2_DW.obj.matlabCodegenIsDeleted = true;
    if ((AAIver2_DW.obj.isInitialized == 1) && AAIver2_DW.obj.isSetupComplete) {
      MW_digitalIO_close(AAIver2_DW.obj.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/ATR_CMP_DETECT' */

  /* Terminate for MATLABSystem: '<Root>/ATR_GND CTRL' */
  if (!AAIver2_DW.obj_e.matlabCodegenIsDeleted) {
    AAIver2_DW.obj_e.matlabCodegenIsDeleted = true;
    if ((AAIver2_DW.obj_e.isInitialized == 1) &&
        AAIver2_DW.obj_e.isSetupComplete) {
      MW_digitalIO_close(AAIver2_DW.obj_e.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/ATR_GND CTRL' */

  /* Terminate for MATLABSystem: '<Root>/ATR_PACE_CTRL' */
  if (!AAIver2_DW.obj_n.matlabCodegenIsDeleted) {
    AAIver2_DW.obj_n.matlabCodegenIsDeleted = true;
    if ((AAIver2_DW.obj_n.isInitialized == 1) &&
        AAIver2_DW.obj_n.isSetupComplete) {
      MW_digitalIO_close(AAIver2_DW.obj_n.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/ATR_PACE_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/FRONTEND_CTRL' */
  if (!AAIver2_DW.obj_j.matlabCodegenIsDeleted) {
    AAIver2_DW.obj_j.matlabCodegenIsDeleted = true;
    if ((AAIver2_DW.obj_j.isInitialized == 1) &&
        AAIver2_DW.obj_j.isSetupComplete) {
      MW_digitalIO_close(AAIver2_DW.obj_j.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/FRONTEND_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */
  if (!AAIver2_DW.obj_lf.matlabCodegenIsDeleted) {
    AAIver2_DW.obj_lf.matlabCodegenIsDeleted = true;
    if ((AAIver2_DW.obj_lf.isInitialized == 1) &&
        AAIver2_DW.obj_lf.isSetupComplete) {
      MW_digitalIO_close(AAIver2_DW.obj_lf.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACE_CHARGE_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/PACE_GND_CTRL' */
  if (!AAIver2_DW.obj_h0.matlabCodegenIsDeleted) {
    AAIver2_DW.obj_h0.matlabCodegenIsDeleted = true;
    if ((AAIver2_DW.obj_h0.isInitialized == 1) &&
        AAIver2_DW.obj_h0.isSetupComplete) {
      MW_digitalIO_close(AAIver2_DW.obj_h0.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACE_GND_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/VENT_PACE_CTRL' */
  if (!AAIver2_DW.obj_h.matlabCodegenIsDeleted) {
    AAIver2_DW.obj_h.matlabCodegenIsDeleted = true;
    if ((AAIver2_DW.obj_h.isInitialized == 1) &&
        AAIver2_DW.obj_h.isSetupComplete) {
      MW_digitalIO_close(AAIver2_DW.obj_h.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/VENT_PACE_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/Z_ATR_CTRL' */
  if (!AAIver2_DW.obj_g.matlabCodegenIsDeleted) {
    AAIver2_DW.obj_g.matlabCodegenIsDeleted = true;
    if ((AAIver2_DW.obj_g.isInitialized == 1) &&
        AAIver2_DW.obj_g.isSetupComplete) {
      MW_digitalIO_close(AAIver2_DW.obj_g.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Z_ATR_CTRL' */

  /* Terminate for MATLABSystem: '<Root>/ATR_CMP_REF_PWM Output' */
  if (!AAIver2_DW.obj_l.matlabCodegenIsDeleted) {
    AAIver2_DW.obj_l.matlabCodegenIsDeleted = true;
    if ((AAIver2_DW.obj_l.isInitialized == 1) &&
        AAIver2_DW.obj_l.isSetupComplete) {
      MW_PWM_Stop(AAIver2_DW.obj_l.MW_PWM_HANDLE);
      MW_PWM_Close(AAIver2_DW.obj_l.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/ATR_CMP_REF_PWM Output' */

  /* Terminate for MATLABSystem: '<Root>/PACING_REF_PWM Output' */
  if (!AAIver2_DW.obj_o.matlabCodegenIsDeleted) {
    AAIver2_DW.obj_o.matlabCodegenIsDeleted = true;
    if ((AAIver2_DW.obj_o.isInitialized == 1) &&
        AAIver2_DW.obj_o.isSetupComplete) {
      MW_PWM_Stop(AAIver2_DW.obj_o.MW_PWM_HANDLE);
      MW_PWM_Close(AAIver2_DW.obj_o.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PACING_REF_PWM Output' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
