from django.shortcuts import render
from django.http import JsonResponse
from .services import execute_query


ADMISIONES = "SC0011"
LIQUIDACIONES = "SC0012"
PACIENTES = "SC0004"
CIAS = "SC0002"
EMPRESAS = "SC0003"
MEDICOS = "SC0006"
FACTURAS = "SC0017"
DEVOLUCIONES = "SC0033"


def get_admisiones(request):
    starDate = request.GET.get('starDate')
    endDate = request.GET.get('endDate')

    # Validar que las fechas existan
    if not starDate or not endDate:
        return JsonResponse({'error': 'starDate and endDate are required'}, status=400)

    query = (
        f"SELECT {ADMISIONES}.num_doc as number, "
        f"{ADMISIONES}.fec_doc as attendance_date, "
        f"{ADMISIONES}.nom_pac as patient, "
        f"{ADMISIONES}.hi_doc as attendance_hour, "
        f"{ADMISIONES}.ta_doc as type, {ADMISIONES}.tot_doc as amount, "
        f"{EMPRESAS}.nom_emp as company, {MEDICOS}.nom_ser as doctor, "
        f"{PACIENTES}.nh_pac medical_record_number, "
        f"{CIAS}.nom_cia insurer_name "
        f"FROM {ADMISIONES} "
        f"LEFT JOIN {MEDICOS} ON {ADMISIONES}.cod_ser = {MEDICOS}.cod_ser "
        f"LEFT JOIN {CIAS} ON LEFT({ADMISIONES}.cod_emp, 2) = {CIAS}.cod_cia "
        f"LEFT JOIN {EMPRESAS} ON {ADMISIONES}.cod_emp = {EMPRESAS}.cod_emp "
        f"LEFT JOIN {PACIENTES} ON {ADMISIONES}.cod_pac = {PACIENTES}.cod_pac "
        f"WHERE fec_doc BETWEEN ctod('{starDate}') AND ctod('{endDate}') "
        f"AND ({CIAS}.nom_cia <> 'PARTICULAR' OR {ADMISIONES}.tot_doc <> 0) "
        f"AND {PACIENTES}.nh_pac IS NOT NULL AND {PACIENTES}.nh_pac <> '' "
        f"AND {ADMISIONES}.nom_pac IS NOT NULL AND {ADMISIONES}.nom_pac <> '' "
        f"ORDER BY {ADMISIONES}.cod_ser ASC;"
    )

    print(query)
    try:

        data = execute_query(query)

        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_admisiones_seguros(request):
    starDate = request.GET.get('starDate')
    endDate = request.GET.get('endDate')

    # Validar que las fechas existan
    if not starDate or not endDate:
        return JsonResponse({'error': 'starDate and endDate are required'}, status=400)

    query = (
        f"SELECT {ADMISIONES}.num_doc as number, "
        f"{ADMISIONES}.fec_doc as attendance_date, "
        f"{ADMISIONES}.nom_pac as patient, "
        f"{ADMISIONES}.hi_doc as attendance_hour, "
        f"{ADMISIONES}.ta_doc as type, {ADMISIONES}.tot_doc as amount, "
        f"{EMPRESAS}.nom_emp as company, {MEDICOS}.nom_ser as doctor, "
        f"{PACIENTES}.nh_pac medical_record_number, "
        f"{ADMISIONES}.clos_doc as is_closed, "
        f"{FACTURAS}.num_fac as invoice_number, "
        f"{FACTURAS}.fec_fac as invoice_date, "
        f"{FACTURAS}.uc_sis as biller, "
        # f"{DEVOLUCIONES}.fh_dev, "
        f"{CIAS}.nom_cia as insurer_name "
        f"FROM {ADMISIONES} "
        f"LEFT JOIN {MEDICOS} ON {ADMISIONES}.cod_ser = {MEDICOS}.cod_ser "
        f"LEFT JOIN {CIAS} ON LEFT({ADMISIONES}.cod_emp, 2) = {CIAS}.cod_cia "
        f"LEFT JOIN {EMPRESAS} ON {ADMISIONES}.cod_emp = {EMPRESAS}.cod_emp "
        f"LEFT JOIN {PACIENTES} ON {ADMISIONES}.cod_pac = {PACIENTES}.cod_pac "
        f"LEFT JOIN {DEVOLUCIONES} ON {
            ADMISIONES}.num_doc = {DEVOLUCIONES}.num_doc "
        f"LEFT JOIN {FACTURAS} ON {ADMISIONES}.num_doc = {FACTURAS}.num_doc "
        f"WHERE "
        f"fec_doc BETWEEN ctod('{starDate}') AND ctod('{
            endDate}') "
        f"AND {CIAS}.nom_cia <> 'PARTICULAR' "
        f"AND {PACIENTES}.nh_pac IS NOT NULL AND {PACIENTES}.nh_pac <> '' "
        f"AND {ADMISIONES}.nom_pac IS NOT NULL AND {ADMISIONES}.nom_pac <> '' "
        f"ORDER BY {ADMISIONES}.cod_ser ASC;"
    )
    # query = (
    #     f"SELECT TOP 10 * "
    #     f"FROM {ADMISIONES} "
    #     f"WHERE {ADMISIONES}.num_doc = '0000304116' "
    #     f"ORDER BY {ADMISIONES}.num_doc ASC"
    # )

    print(query)
    try:

        data = execute_query(query)

        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_pacientes(request):
    starDate = request.GET.get('starDate')
    endDate = request.GET.get('endDate')

    # Validar que las fechas existan
    if not starDate or not endDate:
        return JsonResponse({'error': 'starDate and endDate are required'}, status=400)

    query = (
        f"SELECT TOP 10 * FROM {PACIENTES} "
        "ORDER BY COD_PAC ASC;"
    )

    try:
        data = execute_query(query)

        return JsonResponse(data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_cias(request):
    starDate = request.GET.get('starDate')
    endDate = request.GET.get('endDate')

    # Validar que las fechas existan
    if not starDate or not endDate:
        return JsonResponse({'error': 'starDate and endDate are required'}, status=400)

    query = (
        f"SELECT TOP 10 * FROM {CIAS} "
        "ORDER BY COD_CIA ASC;"
    )

    try:
        data = execute_query(query)

        return JsonResponse(data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_empresas(request):
    starDate = request.GET.get('starDate')
    endDate = request.GET.get('endDate')

    # Validar que las fechas existan
    if not starDate or not endDate:
        return JsonResponse({'error': 'starDate and endDate are required'}, status=400)

    query = (
        f"SELECT TOP 10 * FROM {EMPRESAS} "
        "ORDER BY COD_EMP ASC;"
    )

    try:
        data = execute_query(query)

        return JsonResponse(data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_medicos(request):
    starDate = request.GET.get('starDate')
    endDate = request.GET.get('endDate')

    # Validar que las fechas existan
    if not starDate or not endDate:
        return JsonResponse({'error': 'starDate and endDate are required'}, status=400)

    query = (
        f"SELECT TOP 10 * FROM {MEDICOS} "
        "ORDER BY cod_ser ASC;"
    )

    try:
        data = execute_query(query)

        return JsonResponse(data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_liquidaciones(request):
    starDate = request.GET.get('starDate')
    endDate = request.GET.get('endDate')

    # Validar que las fechas existan
    if not starDate or not endDate:
        return JsonResponse({'error': 'starDate and endDate are required'}, status=400)

    query = (
        f"SELECT TOP 10 * FROM {LIQUIDACIONES} "
        f"WHERE fec_ser BETWEEN ctod('{starDate}') AND ctod('{endDate}') "
        f"ORDER BY cod_ser ASC;"
    )

    print(query)
    try:

        data = execute_query(query)

        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_facturas(request):
    starDate = request.GET.get('starDate')
    endDate = request.GET.get('endDate')

    # Validar que las fechas existan
    if not starDate or not endDate:
        return JsonResponse({'error': 'starDate and endDate are required'}, status=400)

    query = (
        f"SELECT TOP 10 * FROM {FACTURAS} "
        f"ORDER BY num_doc ASC;"
    )

    print(query)
    try:

        data = execute_query(query)

        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_devoluciones(request):
    starDate = request.GET.get('starDate')
    endDate = request.GET.get('endDate')

    # Validar que las fechas existan
    if not starDate or not endDate:
        return JsonResponse({'error': 'starDate and endDate are required'}, status=400)

    query = (
        f"SELECT TOP 10 * FROM {DEVOLUCIONES} "
        f"ORDER BY num_doc ASC;"
    )

    print(query)
    try:

        data = execute_query(query)

        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
