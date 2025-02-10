# paheko_client.DefaultApi

All URIs are relative to *https://votre_association.paheko.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounting_account_get**](DefaultApi.md#accounting_account_get) | **GET** /accounting/account | Récupérer tous les comptes comptables
[**accounting_category_get**](DefaultApi.md#accounting_category_get) | **GET** /accounting/category | Récupérer toutes les catégories comptables
[**accounting_charts_get**](DefaultApi.md#accounting_charts_get) | **GET** /accounting/charts | Récupérer les plans comptables
[**accounting_charts_idchart_accounts_get**](DefaultApi.md#accounting_charts_idchart_accounts_get) | **GET** /accounting/charts/{ID_CHART}/accounts | Récupérer les comptes d&#x27;un plan comptable
[**accounting_transaction_idtransaction_delete**](DefaultApi.md#accounting_transaction_idtransaction_delete) | **DELETE** /accounting/transaction/{ID_TRANSACTION} | Supprimer une transaction
[**accounting_transaction_idtransaction_get**](DefaultApi.md#accounting_transaction_idtransaction_get) | **GET** /accounting/transaction/{ID_TRANSACTION} | Récupérer une transaction
[**accounting_transaction_idtransaction_post**](DefaultApi.md#accounting_transaction_idtransaction_post) | **POST** /accounting/transaction/{ID_TRANSACTION} | Modifier une transaction
[**accounting_transaction_idtransaction_put**](DefaultApi.md#accounting_transaction_idtransaction_put) | **PUT** /accounting/transaction/{ID_TRANSACTION} | Mettre à jour une transaction
[**accounting_transaction_idtransaction_subscriptions_delete**](DefaultApi.md#accounting_transaction_idtransaction_subscriptions_delete) | **DELETE** /accounting/transaction/{ID_TRANSACTION}/subscriptions | Dissocier des inscriptions d&#x27;une écriture
[**accounting_transaction_idtransaction_subscriptions_get**](DefaultApi.md#accounting_transaction_idtransaction_subscriptions_get) | **GET** /accounting/transaction/{ID_TRANSACTION}/subscriptions | Récupérer les inscriptions liées à une écriture
[**accounting_transaction_idtransaction_subscriptions_post**](DefaultApi.md#accounting_transaction_idtransaction_subscriptions_post) | **POST** /accounting/transaction/{ID_TRANSACTION}/subscriptions | Associer des inscriptions à une écriture
[**accounting_transaction_idtransaction_transactions_delete**](DefaultApi.md#accounting_transaction_idtransaction_transactions_delete) | **DELETE** /accounting/transaction/{ID_TRANSACTION}/transactions | Dissocier des écritures d&#x27;une transaction
[**accounting_transaction_idtransaction_transactions_get**](DefaultApi.md#accounting_transaction_idtransaction_transactions_get) | **GET** /accounting/transaction/{ID_TRANSACTION}/transactions | Récupérer les écritures liées à une transaction
[**accounting_transaction_idtransaction_transactions_post**](DefaultApi.md#accounting_transaction_idtransaction_transactions_post) | **POST** /accounting/transaction/{ID_TRANSACTION}/transactions | Associer des écritures à une transaction
[**accounting_transaction_idtransaction_users_delete**](DefaultApi.md#accounting_transaction_idtransaction_users_delete) | **DELETE** /accounting/transaction/{ID_TRANSACTION}/users | Dissocier des utilisateurs d&#x27;une transaction
[**accounting_transaction_idtransaction_users_get**](DefaultApi.md#accounting_transaction_idtransaction_users_get) | **GET** /accounting/transaction/{ID_TRANSACTION}/users | Lister les utilisateurs liés à une transaction
[**accounting_transaction_idtransaction_users_post**](DefaultApi.md#accounting_transaction_idtransaction_users_post) | **POST** /accounting/transaction/{ID_TRANSACTION}/users | Associer une transaction à des utilisateurs
[**accounting_transaction_post**](DefaultApi.md#accounting_transaction_post) | **POST** /accounting/transaction | Créer une transaction comptable
[**accounting_years_get**](DefaultApi.md#accounting_years_get) | **GET** /accounting/years | Récupérer les années comptables
[**accounting_years_idyear_export_formatextension_get**](DefaultApi.md#accounting_years_idyear_export_formatextension_get) | **GET** /accounting/years/{ID_YEAR}/export/{FORMAT}.{EXTENSION} | Exporter un exercice comptable
[**accounting_years_idyear_journal_get**](DefaultApi.md#accounting_years_idyear_journal_get) | **GET** /accounting/years/{ID_YEAR}/journal | Récupérer le journal d&#x27;une année comptable
[**download_files_get**](DefaultApi.md#download_files_get) | **GET** /download/files | Télécharger tous les fichiers
[**download_get**](DefaultApi.md#download_get) | **GET** /download | Télécharger la base de données
[**errors_log_get**](DefaultApi.md#errors_log_get) | **GET** /errors/log | Récupérer le log d&#x27;erreurs système
[**errors_report_post**](DefaultApi.md#errors_report_post) | **POST** /errors/report | Envoyer un rapport d&#x27;erreur
[**services_subscriptions_import_put**](DefaultApi.md#services_subscriptions_import_put) | **PUT** /services/subscriptions/import | Importer les inscriptions des membres aux activités
[**sql_post**](DefaultApi.md#sql_post) | **POST** /sql | Exécuter une requête SQL SELECT
[**user_categories_get**](DefaultApi.md#user_categories_get) | **GET** /user/categories | Récupérer la liste des catégories de membres
[**user_category_idformat_get**](DefaultApi.md#user_category_idformat_get) | **GET** /user/category/{ID}.{FORMAT} | Exporter les membres d&#x27;une catégorie
[**user_iduser_delete**](DefaultApi.md#user_iduser_delete) | **DELETE** /user/{ID_USER} | Supprimer un utilisateur
[**user_iduser_get**](DefaultApi.md#user_iduser_get) | **GET** /user/{ID_USER} | Récupérer un utilisateur
[**user_iduser_post**](DefaultApi.md#user_iduser_post) | **POST** /user/{ID_USER} | Mettre à jour un utilisateur
[**user_iduser_put**](DefaultApi.md#user_iduser_put) | **PUT** /user/{ID_USER} | Mettre à jour un utilisateur
[**user_import_preview_post**](DefaultApi.md#user_import_preview_post) | **POST** /user/import/preview | Prévisualiser un import de membres (POST)
[**user_import_preview_put**](DefaultApi.md#user_import_preview_put) | **PUT** /user/import/preview | Prévisualiser un import de membres
[**user_import_put**](DefaultApi.md#user_import_put) | **PUT** /user/import | Importer une liste de membres
[**user_new_post**](DefaultApi.md#user_new_post) | **POST** /user/new | Créer un nouveau membre
[**web_attachment_pageurifilename_get**](DefaultApi.md#web_attachment_pageurifilename_get) | **GET** /web/attachment/{PAGE_URI}/{FILENAME} | Récupérer un fichier joint d&#x27;une page
[**web_html_pageuri_get**](DefaultApi.md#web_html_pageuri_get) | **GET** /web/html/{PAGE_URI} | Récupérer le contenu HTML d&#x27;une page
[**web_list_get**](DefaultApi.md#web_list_get) | **GET** /web/list | Lister les pages du site web
[**web_page_pageuri_get**](DefaultApi.md#web_page_pageuri_get) | **GET** /web/page/{PAGE_URI} | Récupérer les informations d&#x27;une page

# **accounting_account_get**
> accounting_account_get()

Récupérer tous les comptes comptables

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))

try:
    # Récupérer tous les comptes comptables
    api_instance.accounting_account_get()
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_account_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_category_get**
> accounting_category_get()

Récupérer toutes les catégories comptables

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))

try:
    # Récupérer toutes les catégories comptables
    api_instance.accounting_category_get()
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_category_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_charts_get**
> accounting_charts_get()

Récupérer les plans comptables

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))

try:
    # Récupérer les plans comptables
    api_instance.accounting_charts_get()
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_charts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_charts_idchart_accounts_get**
> accounting_charts_idchart_accounts_get(id_chart)

Récupérer les comptes d'un plan comptable

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_chart = 56 # int | 

try:
    # Récupérer les comptes d'un plan comptable
    api_instance.accounting_charts_idchart_accounts_get(id_chart)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_charts_idchart_accounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_chart** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_transaction_idtransaction_delete**
> accounting_transaction_idtransaction_delete(id_transaction)

Supprimer une transaction

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_transaction = 56 # int | 

try:
    # Supprimer une transaction
    api_instance.accounting_transaction_idtransaction_delete(id_transaction)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_transaction_idtransaction_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_transaction** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_transaction_idtransaction_get**
> accounting_transaction_idtransaction_get(id_transaction)

Récupérer une transaction

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_transaction = 56 # int | 

try:
    # Récupérer une transaction
    api_instance.accounting_transaction_idtransaction_get(id_transaction)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_transaction_idtransaction_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_transaction** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_transaction_idtransaction_post**
> accounting_transaction_idtransaction_post(id_transaction)

Modifier une transaction

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_transaction = 56 # int | 

try:
    # Modifier une transaction
    api_instance.accounting_transaction_idtransaction_post(id_transaction)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_transaction_idtransaction_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_transaction** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_transaction_idtransaction_put**
> accounting_transaction_idtransaction_put(id_transaction, label=label, amount=amount)

Mettre à jour une transaction

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_transaction = 56 # int | 
label = 'label_example' # str |  (optional)
amount = 1.2 # float |  (optional)

try:
    # Mettre à jour une transaction
    api_instance.accounting_transaction_idtransaction_put(id_transaction, label=label, amount=amount)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_transaction_idtransaction_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_transaction** | **int**|  | 
 **label** | **str**|  | [optional] 
 **amount** | **float**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_transaction_idtransaction_subscriptions_delete**
> accounting_transaction_idtransaction_subscriptions_delete(id_transaction)

Dissocier des inscriptions d'une écriture

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_transaction = 56 # int | 

try:
    # Dissocier des inscriptions d'une écriture
    api_instance.accounting_transaction_idtransaction_subscriptions_delete(id_transaction)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_transaction_idtransaction_subscriptions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_transaction** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_transaction_idtransaction_subscriptions_get**
> accounting_transaction_idtransaction_subscriptions_get(id_transaction)

Récupérer les inscriptions liées à une écriture

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_transaction = 56 # int | 

try:
    # Récupérer les inscriptions liées à une écriture
    api_instance.accounting_transaction_idtransaction_subscriptions_get(id_transaction)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_transaction_idtransaction_subscriptions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_transaction** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_transaction_idtransaction_subscriptions_post**
> accounting_transaction_idtransaction_subscriptions_post(subscriptions, id_transaction)

Associer des inscriptions à une écriture

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
subscriptions = [56] # list[int] | 
id_transaction = 56 # int | 

try:
    # Associer des inscriptions à une écriture
    api_instance.accounting_transaction_idtransaction_subscriptions_post(subscriptions, id_transaction)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_transaction_idtransaction_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptions** | [**list[int]**](int.md)|  | 
 **id_transaction** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_transaction_idtransaction_transactions_delete**
> accounting_transaction_idtransaction_transactions_delete(id_transaction)

Dissocier des écritures d'une transaction

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_transaction = 56 # int | 

try:
    # Dissocier des écritures d'une transaction
    api_instance.accounting_transaction_idtransaction_transactions_delete(id_transaction)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_transaction_idtransaction_transactions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_transaction** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_transaction_idtransaction_transactions_get**
> accounting_transaction_idtransaction_transactions_get(id_transaction)

Récupérer les écritures liées à une transaction

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_transaction = 56 # int | 

try:
    # Récupérer les écritures liées à une transaction
    api_instance.accounting_transaction_idtransaction_transactions_get(id_transaction)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_transaction_idtransaction_transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_transaction** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_transaction_idtransaction_transactions_post**
> accounting_transaction_idtransaction_transactions_post(transactions, id_transaction)

Associer des écritures à une transaction

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
transactions = [56] # list[int] | 
id_transaction = 56 # int | 

try:
    # Associer des écritures à une transaction
    api_instance.accounting_transaction_idtransaction_transactions_post(transactions, id_transaction)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_transaction_idtransaction_transactions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactions** | [**list[int]**](int.md)|  | 
 **id_transaction** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_transaction_idtransaction_users_delete**
> accounting_transaction_idtransaction_users_delete(id_transaction)

Dissocier des utilisateurs d'une transaction

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_transaction = 56 # int | 

try:
    # Dissocier des utilisateurs d'une transaction
    api_instance.accounting_transaction_idtransaction_users_delete(id_transaction)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_transaction_idtransaction_users_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_transaction** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_transaction_idtransaction_users_get**
> accounting_transaction_idtransaction_users_get(id_transaction)

Lister les utilisateurs liés à une transaction

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_transaction = 56 # int | 

try:
    # Lister les utilisateurs liés à une transaction
    api_instance.accounting_transaction_idtransaction_users_get(id_transaction)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_transaction_idtransaction_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_transaction** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_transaction_idtransaction_users_post**
> accounting_transaction_idtransaction_users_post(id_transaction)

Associer une transaction à des utilisateurs

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_transaction = 56 # int | 

try:
    # Associer une transaction à des utilisateurs
    api_instance.accounting_transaction_idtransaction_users_post(id_transaction)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_transaction_idtransaction_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_transaction** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_transaction_post**
> accounting_transaction_post(body)

Créer une transaction comptable

Crée une nouvelle transaction comptable avec les paramètres spécifiés.

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
body = paheko_client.AccountingTransactionBody() # AccountingTransactionBody | 

try:
    # Créer une transaction comptable
    api_instance.accounting_transaction_post(body)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_transaction_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountingTransactionBody**](AccountingTransactionBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_years_get**
> accounting_years_get()

Récupérer les années comptables

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))

try:
    # Récupérer les années comptables
    api_instance.accounting_years_get()
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_years_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_years_idyear_export_formatextension_get**
> accounting_years_idyear_export_formatextension_get(id_year, format, extension)

Exporter un exercice comptable

Exporte l'exercice indiqué. Utiliser 'current' pour l'exercice ouvert en cours.

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_year = 'id_year_example' # str | 
format = 'format_example' # str | 
extension = 'extension_example' # str | 

try:
    # Exporter un exercice comptable
    api_instance.accounting_years_idyear_export_formatextension_get(id_year, format, extension)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_years_idyear_export_formatextension_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_year** | **str**|  | 
 **format** | **str**|  | 
 **extension** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_years_idyear_journal_get**
> accounting_years_idyear_journal_get(id_year, code=code, id=id)

Récupérer le journal d'une année comptable

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_year = 'id_year_example' # str | ID de l'exercice ou 'current' pour l'exercice en cours.
code = 'code_example' # str |  (optional)
id = 56 # int |  (optional)

try:
    # Récupérer le journal d'une année comptable
    api_instance.accounting_years_idyear_journal_get(id_year, code=code, id=id)
except ApiException as e:
    print("Exception when calling DefaultApi->accounting_years_idyear_journal_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_year** | **str**| ID de l&#x27;exercice ou &#x27;current&#x27; pour l&#x27;exercice en cours. | 
 **code** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_files_get**
> download_files_get()

Télécharger tous les fichiers

Télécharge un fichier ZIP contenant tous les fichiers associés (documents, fichiers des écritures, des membres, etc.).

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))

try:
    # Télécharger tous les fichiers
    api_instance.download_files_get()
except ApiException as e:
    print("Exception when calling DefaultApi->download_files_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_get**
> download_get()

Télécharger la base de données

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))

try:
    # Télécharger la base de données
    api_instance.download_get()
except ApiException as e:
    print("Exception when calling DefaultApi->download_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **errors_log_get**
> errors_log_get()

Récupérer le log d'erreurs système

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))

try:
    # Récupérer le log d'erreurs système
    api_instance.errors_log_get()
except ApiException as e:
    print("Exception when calling DefaultApi->errors_log_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **errors_report_post**
> errors_report_post()

Envoyer un rapport d'erreur

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))

try:
    # Envoyer un rapport d'erreur
    api_instance.errors_report_post()
except ApiException as e:
    print("Exception when calling DefaultApi->errors_report_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_subscriptions_import_put**
> services_subscriptions_import_put(file)

Importer les inscriptions des membres aux activités

Permet d'importer un fichier CSV des inscriptions des membres aux activités.

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
file = 'file_example' # str | 

try:
    # Importer les inscriptions des membres aux activités
    api_instance.services_subscriptions_import_put(file)
except ApiException as e:
    print("Exception when calling DefaultApi->services_subscriptions_import_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sql_post**
> sql_post(sql, format)

Exécuter une requête SQL SELECT

Permet d'exécuter une requête SQL SELECT sur la base de données (aucune requête d'écriture n'est autorisée).

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
sql = 'sql_example' # str | 
format = 'format_example' # str | 

try:
    # Exécuter une requête SQL SELECT
    api_instance.sql_post(sql, format)
except ApiException as e:
    print("Exception when calling DefaultApi->sql_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql** | **str**|  | 
 **format** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_categories_get**
> user_categories_get()

Récupérer la liste des catégories de membres

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))

try:
    # Récupérer la liste des catégories de membres
    api_instance.user_categories_get()
except ApiException as e:
    print("Exception when calling DefaultApi->user_categories_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_category_idformat_get**
> user_category_idformat_get(id, format)

Exporter les membres d'une catégorie

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id = 56 # int | 
format = 'format_example' # str | 

try:
    # Exporter les membres d'une catégorie
    api_instance.user_category_idformat_get(id, format)
except ApiException as e:
    print("Exception when calling DefaultApi->user_category_idformat_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_iduser_delete**
> user_iduser_delete(id_user)

Supprimer un utilisateur

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_user = 56 # int | 

try:
    # Supprimer un utilisateur
    api_instance.user_iduser_delete(id_user)
except ApiException as e:
    print("Exception when calling DefaultApi->user_iduser_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_user** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_iduser_get**
> user_iduser_get(id_user)

Récupérer un utilisateur

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_user = 56 # int | 

try:
    # Récupérer un utilisateur
    api_instance.user_iduser_get(id_user)
except ApiException as e:
    print("Exception when calling DefaultApi->user_iduser_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_user** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_iduser_post**
> user_iduser_post(id_user, nom=nom, prenom=prenom)

Mettre à jour un utilisateur

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_user = 56 # int | 
nom = 'nom_example' # str |  (optional)
prenom = 'prenom_example' # str |  (optional)

try:
    # Mettre à jour un utilisateur
    api_instance.user_iduser_post(id_user, nom=nom, prenom=prenom)
except ApiException as e:
    print("Exception when calling DefaultApi->user_iduser_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_user** | **int**|  | 
 **nom** | **str**|  | [optional] 
 **prenom** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_iduser_put**
> user_iduser_put(id_user, email=email, id_category=id_category)

Mettre à jour un utilisateur

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
id_user = 56 # int | 
email = 'email_example' # str |  (optional)
id_category = 56 # int |  (optional)

try:
    # Mettre à jour un utilisateur
    api_instance.user_iduser_put(id_user, email=email, id_category=id_category)
except ApiException as e:
    print("Exception when calling DefaultApi->user_iduser_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_user** | **int**|  | 
 **email** | **str**|  | [optional] 
 **id_category** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_import_preview_post**
> user_import_preview_post(file)

Prévisualiser un import de membres (POST)

Identique à PUT, mais avec paramètres dans le corps.

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
file = 'file_example' # str | 

try:
    # Prévisualiser un import de membres (POST)
    api_instance.user_import_preview_post(file)
except ApiException as e:
    print("Exception when calling DefaultApi->user_import_preview_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_import_preview_put**
> user_import_preview_put(file)

Prévisualiser un import de membres

Permet de simuler un import et d'afficher les erreurs ou modifications avant l'importation réelle.

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
file = 'file_example' # str | 

try:
    # Prévisualiser un import de membres
    api_instance.user_import_preview_put(file)
except ApiException as e:
    print("Exception when calling DefaultApi->user_import_preview_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_import_put**
> user_import_put(file, mode=mode, skip_lines=skip_lines, column_0=column_0, column_1=column_1, column_2=column_2, column_3=column_3, column_4=column_4)

Importer une liste de membres

Permet d'importer un fichier CSV/XLSX/ODS de la liste des membres.

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
file = 'file_example' # str | 
mode = 'mode_example' # str |  (optional)
skip_lines = 56 # int | Nombre de lignes à ignorer (optional)
column_0 = 'column_0_example' # str | Correspondance de la colonne 0 (optional)
column_1 = 'column_1_example' # str | Correspondance de la colonne 1 (optional)
column_2 = 'column_2_example' # str | Correspondance de la colonne 2 (optional)
column_3 = 'column_3_example' # str | Correspondance de la colonne 3 (optional)
column_4 = 'column_4_example' # str | Correspondance de la colonne 4 (optional)

try:
    # Importer une liste de membres
    api_instance.user_import_put(file, mode=mode, skip_lines=skip_lines, column_0=column_0, column_1=column_1, column_2=column_2, column_3=column_3, column_4=column_4)
except ApiException as e:
    print("Exception when calling DefaultApi->user_import_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **mode** | **str**|  | [optional] 
 **skip_lines** | **int**| Nombre de lignes à ignorer | [optional] 
 **column_0** | **str**| Correspondance de la colonne 0 | [optional] 
 **column_1** | **str**| Correspondance de la colonne 1 | [optional] 
 **column_2** | **str**| Correspondance de la colonne 2 | [optional] 
 **column_3** | **str**| Correspondance de la colonne 3 | [optional] 
 **column_4** | **str**| Correspondance de la colonne 4 | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_new_post**
> user_new_post(nom, prenom, email, id_category, password)

Créer un nouveau membre

Ajoute un nouvel utilisateur à l'association.

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
nom = 'nom_example' # str | 
prenom = 'prenom_example' # str | 
email = 'email_example' # str | 
id_category = 56 # int | 
password = 'password_example' # str | 

try:
    # Créer un nouveau membre
    api_instance.user_new_post(nom, prenom, email, id_category, password)
except ApiException as e:
    print("Exception when calling DefaultApi->user_new_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nom** | **str**|  | 
 **prenom** | **str**|  | 
 **email** | **str**|  | 
 **id_category** | **int**|  | 
 **password** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_attachment_pageurifilename_get**
> web_attachment_pageurifilename_get(page_uri, filename)

Récupérer un fichier joint d'une page

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
page_uri = 'page_uri_example' # str | 
filename = 'filename_example' # str | 

try:
    # Récupérer un fichier joint d'une page
    api_instance.web_attachment_pageurifilename_get(page_uri, filename)
except ApiException as e:
    print("Exception when calling DefaultApi->web_attachment_pageurifilename_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_uri** | **str**|  | 
 **filename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_html_pageuri_get**
> web_html_pageuri_get(page_uri)

Récupérer le contenu HTML d'une page

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
page_uri = 'page_uri_example' # str | 

try:
    # Récupérer le contenu HTML d'une page
    api_instance.web_html_pageuri_get(page_uri)
except ApiException as e:
    print("Exception when calling DefaultApi->web_html_pageuri_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_uri** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_list_get**
> web_list_get()

Lister les pages du site web

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))

try:
    # Lister les pages du site web
    api_instance.web_list_get()
except ApiException as e:
    print("Exception when calling DefaultApi->web_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_page_pageuri_get**
> web_page_pageuri_get(page_uri)

Récupérer les informations d'une page

### Example
```python
from __future__ import print_function
import time
import paheko_client
from paheko_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = paheko_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = paheko_client.DefaultApi(paheko_client.ApiClient(configuration))
page_uri = 'page_uri_example' # str | 

try:
    # Récupérer les informations d'une page
    api_instance.web_page_pageuri_get(page_uri)
except ApiException as e:
    print("Exception when calling DefaultApi->web_page_pageuri_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_uri** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

