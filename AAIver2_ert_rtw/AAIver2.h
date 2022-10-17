/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: AAIver2.h
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

#ifndef RTW_HEADER_AAIver2_h_
#define RTW_HEADER_AAIver2_h_
#ifndef AAIver2_COMMON_INCLUDES_
#define AAIver2_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "MW_digitalIO.h"
#include "MW_PWM.h"
#endif                                 /* AAIver2_COMMON_INCLUDES_ */

#include "AAIver2_types.h"
#include <stddef.h>

/* Macros for accessing real-time model data structure */
#ifndef rtmGetErrorStatus
#define rtmGetErrorStatus(rtm)         ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
#define rtmSetErrorStatus(rtm, val)    ((rtm)->errorStatus = (val))
#endif

/* Block signals (default storage) */
typedef struct {
  real_T cycle_time;                   /* '<S1>/cycle_time_calc' */
  boolean_T PACE_CHARGE_CTRL;          /* '<S1>/Chart1' */
  boolean_T Z_ATR_CTRL;                /* '<S1>/Chart1' */
  boolean_T PACE_GND_CTRL;             /* '<S1>/Chart1' */
  boolean_T ATR_PACE_CTRL;             /* '<S1>/Chart1' */
  boolean_T ATR_GND_CTRL;              /* '<S1>/Chart1' */
  boolean_T VENT_PACE_CTRL;            /* '<S1>/Chart1' */
  boolean_T FRONTEND_CTRL;             /* '<S1>/Chart1' */
} B_AAIver2_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  freedomk64f_DigitalRead_AAIve_T obj; /* '<Root>/ATR_CMP_DETECT' */
  freedomk64f_PWMOutput_AAIver2_T obj_o;/* '<Root>/PACING_REF_PWM Output' */
  freedomk64f_PWMOutput_AAIver2_T obj_l;/* '<Root>/ATR_CMP_REF_PWM Output' */
  freedomk64f_DigitalWrite_AAIv_T obj_g;/* '<Root>/Z_ATR_CTRL' */
  freedomk64f_DigitalWrite_AAIv_T obj_h;/* '<Root>/VENT_PACE_CTRL' */
  freedomk64f_DigitalWrite_AAIv_T obj_h0;/* '<Root>/PACE_GND_CTRL' */
  freedomk64f_DigitalWrite_AAIv_T obj_lf;/* '<Root>/PACE_CHARGE_CTRL' */
  freedomk64f_DigitalWrite_AAIv_T obj_j;/* '<Root>/FRONTEND_CTRL' */
  freedomk64f_DigitalWrite_AAIv_T obj_n;/* '<Root>/ATR_PACE_CTRL' */
  freedomk64f_DigitalWrite_AAIv_T obj_e;/* '<Root>/ATR_GND CTRL' */
  uint32_T temporalCounter_i1;         /* '<S1>/Chart1' */
  uint8_T is_active_c1_AAIver2;        /* '<S1>/cycle_time_calc' */
  uint8_T is_active_c4_AAIver2;        /* '<S1>/Chart1' */
  uint8_T is_c4_AAIver2;               /* '<S1>/Chart1' */
} DW_AAIver2_T;

/* Parameters (default storage) */
struct P_AAIver2_T_ {
  real_T ATR_CMP_DETECT_SampleTime;    /* Expression: SampleTime
                                        * Referenced by: '<Root>/ATR_CMP_DETECT'
                                        */
  real_T p_aPaceWidth_Value;           /* Expression: 30
                                        * Referenced by: '<Root>/p_aPaceWidth'
                                        */
  real_T p_lowrateinterval_Value;      /* Expression: 100
                                        * Referenced by: '<Root>/p_lowrateinterval'
                                        */
  real_T p_ARP_Value;                  /* Expression: 200
                                        * Referenced by: '<Root>/p_ARP'
                                        */
  real_T ATR_CMP_REF_PWM_Value;        /* Expression: 70
                                        * Referenced by: '<Root>/ATR_CMP_REF_PWM'
                                        */
  real_T PACING_REF_PWM_Value;         /* Expression: 50
                                        * Referenced by: '<Root>/PACING_REF_PWM'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_AAIver2_T {
  const char_T * volatile errorStatus;
};

/* Block parameters (default storage) */
extern P_AAIver2_T AAIver2_P;

/* Block signals (default storage) */
extern B_AAIver2_T AAIver2_B;

/* Block states (default storage) */
extern DW_AAIver2_T AAIver2_DW;

/* Model entry point functions */
extern void AAIver2_initialize(void);
extern void AAIver2_step(void);
extern void AAIver2_terminate(void);

/* Real-time Model object */
extern RT_MODEL_AAIver2_T *const AAIver2_M;

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'AAIver2'
 * '<S1>'   : 'AAIver2/AAI_Logic'
 * '<S2>'   : 'AAIver2/AAI_Logic/Chart1'
 * '<S3>'   : 'AAIver2/AAI_Logic/cycle_time_calc'
 */
#endif                                 /* RTW_HEADER_AAIver2_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
