/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: AAIver2_types.h
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

#ifndef RTW_HEADER_AAIver2_types_h_
#define RTW_HEADER_AAIver2_types_h_
#include "rtwtypes.h"
#include "MW_SVD.h"

/* Model Code Variants */

/* Custom Type definition for MATLABSystem: '<Root>/Z_ATR_CTRL' */
#include "MW_SVD.h"
#ifndef struct_tag_0QIIqIWUIOhUbf1p9QN9pB
#define struct_tag_0QIIqIWUIOhUbf1p9QN9pB

struct tag_0QIIqIWUIOhUbf1p9QN9pB
{
  int32_T __dummy;
};

#endif                                 /* struct_tag_0QIIqIWUIOhUbf1p9QN9pB */

#ifndef typedef_b_freedomk64f_Hardware_AAIver_T
#define typedef_b_freedomk64f_Hardware_AAIver_T

typedef struct tag_0QIIqIWUIOhUbf1p9QN9pB b_freedomk64f_Hardware_AAIver_T;

#endif                             /* typedef_b_freedomk64f_Hardware_AAIver_T */

#ifndef struct_tag_q6HQSF2nXq6EjCNj0vbuLD
#define struct_tag_q6HQSF2nXq6EjCNj0vbuLD

struct tag_q6HQSF2nXq6EjCNj0vbuLD
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_AAIver_T Hw;
  MW_Handle_Type MW_DIGITALIO_HANDLE;
  real_T SampleTime;
};

#endif                                 /* struct_tag_q6HQSF2nXq6EjCNj0vbuLD */

#ifndef typedef_freedomk64f_DigitalRead_AAIve_T
#define typedef_freedomk64f_DigitalRead_AAIve_T

typedef struct tag_q6HQSF2nXq6EjCNj0vbuLD freedomk64f_DigitalRead_AAIve_T;

#endif                             /* typedef_freedomk64f_DigitalRead_AAIve_T */

#ifndef struct_tag_RYgVoAXTz61tXGMaBAGv7F
#define struct_tag_RYgVoAXTz61tXGMaBAGv7F

struct tag_RYgVoAXTz61tXGMaBAGv7F
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_AAIver_T Hw;
  MW_Handle_Type MW_PWM_HANDLE;
};

#endif                                 /* struct_tag_RYgVoAXTz61tXGMaBAGv7F */

#ifndef typedef_freedomk64f_PWMOutput_AAIver2_T
#define typedef_freedomk64f_PWMOutput_AAIver2_T

typedef struct tag_RYgVoAXTz61tXGMaBAGv7F freedomk64f_PWMOutput_AAIver2_T;

#endif                             /* typedef_freedomk64f_PWMOutput_AAIver2_T */

#ifndef struct_tag_EkIWEs70Gs0LyfeXELZ2TC
#define struct_tag_EkIWEs70Gs0LyfeXELZ2TC

struct tag_EkIWEs70Gs0LyfeXELZ2TC
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_AAIver_T Hw;
  MW_Handle_Type MW_DIGITALIO_HANDLE;
};

#endif                                 /* struct_tag_EkIWEs70Gs0LyfeXELZ2TC */

#ifndef typedef_freedomk64f_DigitalWrite_AAIv_T
#define typedef_freedomk64f_DigitalWrite_AAIv_T

typedef struct tag_EkIWEs70Gs0LyfeXELZ2TC freedomk64f_DigitalWrite_AAIv_T;

#endif                             /* typedef_freedomk64f_DigitalWrite_AAIv_T */

/* Parameters (default storage) */
typedef struct P_AAIver2_T_ P_AAIver2_T;

/* Forward declaration for rtModel */
typedef struct tag_RTM_AAIver2_T RT_MODEL_AAIver2_T;

#endif                                 /* RTW_HEADER_AAIver2_types_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
