import sqlvalidator
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

teradata_sql_keywords = ["INSERT", "SELECT", "GROUP"]

def validate_sql():
    sql_params = sql.split("\n")

    sql_values_list = []
    for param in sql_params:
        print(param)
        params = param.split(" ")
        sql_values_list.append(params)
        print()

    subqueries = []
    print("\n")
    subquery = ""
    for value_list in sql_values_list:
        for value in value_list:
            print(value)
            if value in teradata_sql_keywords:
                subqueries.append(subquery)
                subquery = ""
                subquery += value + " "
                print("Value {} found in teradata sql".format(value))
            else:
                subquery += value + " "

    subqueries.append(subquery) #Appending the last subquery
    print()

    print("SUBQUERIES")
    for query in subqueries:
        print(query)
        print()



    """sql_query_values = sqlvalidator.parse("Select * from table")

    if not sql_query_values.is_valid():
        print(sql_query_values.errors)"""



if __name__ == '__main__':
    validate_sql()