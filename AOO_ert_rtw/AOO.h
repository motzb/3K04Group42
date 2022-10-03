/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: AOO.h
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

#ifndef RTW_HEADER_AOO_h_
#define RTW_HEADER_AOO_h_
#ifndef AOO_COMMON_INCLUDES_
#define AOO_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "MW_digitalIO.h"
#include "MW_PWM.h"
#endif                                 /* AOO_COMMON_INCLUDES_ */

#include "AOO_types.h"
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
  boolean_T Z_ATR_CTRL;                /* '<Root>/Chart' */
} B_AOO_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  freedomk64f_DigitalWrite_AOO_T obj;  /* '<Root>/Z_ATR_CTRL' */
  freedomk64f_DigitalWrite_AOO_T obj_k;/* '<Root>/PACE_GND_CTRL' */
  freedomk64f_DigitalWrite_AOO_T obj_n;/* '<Root>/PACE_CHARGE_CTRL' */
  freedomk64f_DigitalWrite_AOO_T obj_l;/* '<Root>/ATR_PACE_CTRL' */
  freedomk64f_DigitalWrite_AOO_T obj_e;/* '<Root>/ATR_GND CTRL' */
  freedomk64f_PWMOutput_AOO_T obj_j;   /* '<Root>/PACING_REF_PWM' */
  uint32_T temporalCounter_i1;         /* '<Root>/Chart' */
  uint8_T is_active_c1_AOO;            /* '<Root>/Chart' */
  uint8_T is_c1_AOO;                   /* '<Root>/Chart' */
} DW_AOO_T;

/* Parameters (default storage) */
struct P_AOO_T_ {
  real_T p_lowrateinterval_Value;      /* Expression: 100
                                        * Referenced by: '<Root>/p_lowrateinterval'
                                        */
  real_T p_aPaceWidth_Value;           /* Expression: 1
                                        * Referenced by: '<Root>/p_aPaceWidth'
                                        */
  real_T p_aPaceAmp_Value;             /* Expression: 100
                                        * Referenced by: '<Root>/p_aPaceAmp'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_AOO_T {
  const char_T * volatile errorStatus;
};

/* Block parameters (default storage) */
extern P_AOO_T AOO_P;

/* Block signals (default storage) */
extern B_AOO_T AOO_B;

/* Block states (default storage) */
extern DW_AOO_T AOO_DW;

/* Model entry point functions */
extern void AOO_initialize(void);
extern void AOO_step(void);
extern void AOO_terminate(void);

/* Real-time Model object */
extern RT_MODEL_AOO_T *const AOO_M;

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
 * '<Root>' : 'AOO'
 * '<S1>'   : 'AOO/Chart'
 * '<S2>'   : 'AOO/Requirements Table'
 */
#endif                                 /* RTW_HEADER_AOO_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
