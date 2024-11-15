from django.shortcuts import render
from django.db import connection

def stored_procedure_view(request):
    param1 = 30711
    param2 = 'S'
    results = None
    
    # Execute the stored procedure
    with connection.cursor() as cursor:
        sql = "CALL QSYS_BTS_SponList(%s, %s)"
        
        try:
            cursor.execute(sql, [param1, param2])
            results = cursor.fetchall()  # Fetch all rows from the stored procedure result
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
    
    # Pass results to the template
    return render(request, 'test.html', {'results': results})
