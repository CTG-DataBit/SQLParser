#import sqlvalidator
sql = """INSERT INTO L_DLY1_EMDW_KENDB.TMP_B18_W04
(
CDE_ACC_NO,
ACCR_TO_DTE
)
SELECT
CDE_ACC_NO,
SUM (ACCR_TO_DTE)AS ACCR_TO_DTE
FROM A_EMDW_KENDB.FCTINTSUM_KEB18_TMP_B18_W05
GROUP BY 1"""

def validate_sql():
    sql_params = sql.split("\n")

    sql_values = []
    for param in sql_params:
        print(param)
        params = param.split(" ")
        sql_values.append(params)
        print()

    print("\n")
    for value in sql_values:
        print(value)
        print()
    """sql_query = sqlvalidator.parse("Select * from table oierhgewhr")

    if not sql_query.is_valid():
        print(sql_query.errors)"""



if __name__ == '__main__':
    validate_sql()