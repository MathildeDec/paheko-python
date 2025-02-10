# AccountingTransactionBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_year** | **int** | ID de l&#x27;exercice comptable | 
**label** | **str** | Libellé de la transaction | 
**_date** | **date** | Date au format YYYY-MM-DD | 
**type** | **str** | Type de transaction | [optional] 
**amount** | **float** | Montant (pour transactions simplifiées) | [optional] 
**credit** | **str** | Compte crédité (numéro) | [optional] 
**debit** | **str** | Compte débité (numéro) | [optional] 
**lines** | [**list[AccountingtransactionLines]**](AccountingtransactionLines.md) | Lignes comptables (pour ADVANCED) | [optional] 
**reference** | **str** | Numéro de pièce comptable | [optional] 
**linked_users** | **list[int]** | IDs des membres liés (depuis 1.3.3) | [optional] 
**linked_transactions** | **list[int]** | IDs des transactions liées (depuis 1.3.5) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

