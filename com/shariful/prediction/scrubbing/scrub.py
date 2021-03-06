import pandas as pd
def scrubData(df):
    df.drop([
        'w_id',
        'hl_id',
        'client_w_id',
        'state',
        'district'
    ], 1, inplace=True)
    df.drop([
        'psu_id',
        'house_no',
        'house_hold_no',
        'year_of_intr',
        'month_of_intr',
        'date_of_intr'
    ], 1, inplace=True)

    df.drop([
        'stratum_code'
    ], 1, inplace=True)
    df.drop([
        'serial_no'
    ], 1, inplace=True)

    df.drop([
        'other_int_code',
        'identifcation_code',
        'w_expall_status',
        'w_status', 'twsi_id',
        'client_twsi_id'
    ], 1, inplace=True)
    df.drop([
        'fid',
        'hh_id',
        'client_hh_id',
        'member_identity',
        'father_serial_no',
        'mother_serial_no'
    ], 1, inplace=True)
    df.drop([
        'client_hl_id',
        'building_no',
        'hl_expall_status'
    ], 1, inplace=True)
    df.drop([
        'ever_born'
    ], 1, inplace=True)
    df.drop([
        'fidx',
        'as',
        'as_binned'
    ], 1, inplace=True)
    df.drop([
        'fidh',
        'cdoi',
        'anym',
        'catage1'
    ], 1, inplace=True)

    df.drop([
        'healthscheme_1',
        'healthscheme_2'
    ], 1, inplace=True)

    df.drop([
        'isdeadmigrated'
    ], 1, inplace=True)

    df.drop([
        'isnewrecord',
        'recordupdatedcount',
        'recordupdatedcount',
        'schedule_id',
        'year',
        'id'
    ], 1, inplace=True)

    df.drop([
        'date_of_marriage',
        'month_of_marriage',
        'year_of_marriage'
    ], 1, inplace=True)

    df.drop([
        'year_of_birth',
        'month_of_birth',
        'date_of_birth'
    ], 1, inplace=True)
    df.drop([
        'compensation_after_ster',
        'received_compensation_after_ster',
        'received_compensation_ster_rs'
    ], 1,
        inplace=True)

    df.drop([
        'last_preg_no',
        'previous_last_preg_no',
        'second_last_preg_no',
        'third_last_preg_no'
    ], 1, inplace=True)

    df.drop([
        # 'id'
        'surviving_female'
        , 'surviving_male'
        , 'surviving_total'
        , 'edt'
        , 'occupation'
        , 'marital'
        , 'modern'
        , 'traditional'
        , 'currently_widow'
        , 'is_condom'
        , 'is_anc_registered'
        , 'willing_to_get_pregnant'
        , 'is_currently_menstruating'
        , 'is_any_fp_methos_used'
        , 'fp_method_used'
        , 'source_of_treatment_for_fp'
        , 'how_long_using_this_method'
        , 'method_obtain_last_time'
        , 'reason_for_not_using_fp_method'
        , 'is_method_used_in_last_5_yrs'
        , 'method_type_used_in_last_5_yrs'
        , 'reason_for_discontinuation'
        , 'intend_to_use_fp_method_in_futur'
        , 'when_method_is_going_to_use'
        , 'which_method_going_to_pefer_for_'
        , 'want_more_childern'
        , 'next_child_preference'
        , 'time_for_next_child'
        , 'twsi_expall_status'
        , 'currently_dead_or_out_migrated'
        , 'hh_serial_no'
        , 'usual_residance'
        , 'relation_to_head'
        , 'religion'
        , 'social_group_code'
        , 'currently_attending_school'
        , 'reason_for_not_attending_school'
        , 'status'
        , 'hh_expall_status'
        , 'house_status'
        , 'house_structure'
        , 'owner_status'
        , 'household_have_electricity'
        , 'lighting_source'
        , 'cooking_fuel'
        , 'no_of_dwelling_rooms'
        , 'kitchen_availability'
        , 'is_radio'
        , 'is_television'
        , 'is_computer'
        , 'is_telephone'
        , 'is_washing_machine'
        , 'is_refrigerator'
        , 'is_sewing_machine'
        , 'is_bicycle'
        , 'is_scooter'
        , 'is_car'
        , 'is_tractor'
        , 'is_water_pump'
        , 'cart'
        , 'land_possessed'
        , 'sn'
        , 'current_mar_status'
        , 'is_vasectomy'
        , 'residancial_status'
        , 'iscoveredbyhealthscheme'
        , 'housestatus'
        , 'householdstatus'
        , 'isheadchanged'
        , 'headname'
        , 'rtelephoneno'
        , 'respondentname'
        , 'recordstatus'
        , 'new_born_alive_female'
        , 'new_born_alive_male'
        , 'new_born_alive_total'
        , 'new_surviving_female'
        , 'new_surviving_male'
        , 'new_surviving_total'
        , 'treatment_source'
        , 'regular_treatment_source'
        , 'regular_treatment'
        , 'v204'
        , 'months_of_preg_first_anc'
    ], 1, inplace=True)

    # df.to_numeric(convert_numeric=True)
    # df = df.drop(df[df.astype(float).isnull()].index)
    df.fillna(0, inplace=True)
    df = df[df.result_of_interview == 1]
    df.drop(['result_of_interview'], 1, inplace=True)
    df = df[df.sex == 2]
    df.drop(['sex'], 1, inplace=True)
    df = df[df.outcome_pregnancy != 0]
    df = df[df.anm_in_last_3_months != 0]
    df['outcome_pregnancy'].replace(2, 0, inplace=True)
    df['age'] = df['age'].astype(float)
    df['rural'] = df['rural'].astype(float)
    df['marital_status'] = df['marital_status'].astype(float)
    df['outcome_pregnancy'] = df['outcome_pregnancy'].astype(int)

    return df

def addMissingColumn(df):

    current_col=df.columns
    odisha_path = '../../../data/used_data/AHS_Woman_18_Assam.csv'
    odisha_data = pd.read_csv(odisha_path, delimiter='|', nrows=1)
    data=scrubData(odisha_data)
    data = data.drop("outcome_pregnancy", axis=1)
    data2 = data.drop(current_col, axis=1)
    df=df.append(data2, ignore_index=True)
    df.fillna(0,inplace=True)
    df = df[data.columns]
    df=df.drop(1)
    # df = df[df.is_currently_pregnant == 1]
    df["is_currently_pregnant"]=df["is_currently_pregnant"].replace(0,1)
    # df = df[df.sex == 2]
    print(df.head())
    # df=pd.to_numeric(df, errors='coerce')
    df=df.astype('float')

    return df
