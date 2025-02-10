# coding: utf-8

"""
    Paheko API

    Documentation Swagger pour l'API de Paheko  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/paheko-api/paheko-codegen.git
"""

from __future__ import absolute_import

import unittest

import paheko_client
from paheko_client.api.default_api import DefaultApi  # noqa: E501
from paheko_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accounting_account_get(self):
        """Test case for accounting_account_get

        Récupérer tous les comptes comptables  # noqa: E501
        """
        pass

    def test_accounting_category_get(self):
        """Test case for accounting_category_get

        Récupérer toutes les catégories comptables  # noqa: E501
        """
        pass

    def test_accounting_charts_get(self):
        """Test case for accounting_charts_get

        Récupérer les plans comptables  # noqa: E501
        """
        pass

    def test_accounting_charts_idchart_accounts_get(self):
        """Test case for accounting_charts_idchart_accounts_get

        Récupérer les comptes d'un plan comptable  # noqa: E501
        """
        pass

    def test_accounting_transaction_idtransaction_delete(self):
        """Test case for accounting_transaction_idtransaction_delete

        Supprimer une transaction  # noqa: E501
        """
        pass

    def test_accounting_transaction_idtransaction_get(self):
        """Test case for accounting_transaction_idtransaction_get

        Récupérer une transaction  # noqa: E501
        """
        pass

    def test_accounting_transaction_idtransaction_post(self):
        """Test case for accounting_transaction_idtransaction_post

        Modifier une transaction  # noqa: E501
        """
        pass

    def test_accounting_transaction_idtransaction_put(self):
        """Test case for accounting_transaction_idtransaction_put

        Mettre à jour une transaction  # noqa: E501
        """
        pass

    def test_accounting_transaction_idtransaction_subscriptions_delete(self):
        """Test case for accounting_transaction_idtransaction_subscriptions_delete

        Dissocier des inscriptions d'une écriture  # noqa: E501
        """
        pass

    def test_accounting_transaction_idtransaction_subscriptions_get(self):
        """Test case for accounting_transaction_idtransaction_subscriptions_get

        Récupérer les inscriptions liées à une écriture  # noqa: E501
        """
        pass

    def test_accounting_transaction_idtransaction_subscriptions_post(self):
        """Test case for accounting_transaction_idtransaction_subscriptions_post

        Associer des inscriptions à une écriture  # noqa: E501
        """
        pass

    def test_accounting_transaction_idtransaction_transactions_delete(self):
        """Test case for accounting_transaction_idtransaction_transactions_delete

        Dissocier des écritures d'une transaction  # noqa: E501
        """
        pass

    def test_accounting_transaction_idtransaction_transactions_get(self):
        """Test case for accounting_transaction_idtransaction_transactions_get

        Récupérer les écritures liées à une transaction  # noqa: E501
        """
        pass

    def test_accounting_transaction_idtransaction_transactions_post(self):
        """Test case for accounting_transaction_idtransaction_transactions_post

        Associer des écritures à une transaction  # noqa: E501
        """
        pass

    def test_accounting_transaction_idtransaction_users_delete(self):
        """Test case for accounting_transaction_idtransaction_users_delete

        Dissocier des utilisateurs d'une transaction  # noqa: E501
        """
        pass

    def test_accounting_transaction_idtransaction_users_get(self):
        """Test case for accounting_transaction_idtransaction_users_get

        Lister les utilisateurs liés à une transaction  # noqa: E501
        """
        pass

    def test_accounting_transaction_idtransaction_users_post(self):
        """Test case for accounting_transaction_idtransaction_users_post

        Associer une transaction à des utilisateurs  # noqa: E501
        """
        pass

    def test_accounting_transaction_post(self):
        """Test case for accounting_transaction_post

        Créer une transaction comptable  # noqa: E501
        """
        pass

    def test_accounting_years_get(self):
        """Test case for accounting_years_get

        Récupérer les années comptables  # noqa: E501
        """
        pass

    def test_accounting_years_idyear_export_formatextension_get(self):
        """Test case for accounting_years_idyear_export_formatextension_get

        Exporter un exercice comptable  # noqa: E501
        """
        pass

    def test_accounting_years_idyear_journal_get(self):
        """Test case for accounting_years_idyear_journal_get

        Récupérer le journal d'une année comptable  # noqa: E501
        """
        pass

    def test_download_files_get(self):
        """Test case for download_files_get

        Télécharger tous les fichiers  # noqa: E501
        """
        pass

    def test_download_get(self):
        """Test case for download_get

        Télécharger la base de données  # noqa: E501
        """
        pass

    def test_errors_log_get(self):
        """Test case for errors_log_get

        Récupérer le log d'erreurs système  # noqa: E501
        """
        pass

    def test_errors_report_post(self):
        """Test case for errors_report_post

        Envoyer un rapport d'erreur  # noqa: E501
        """
        pass

    def test_services_subscriptions_import_put(self):
        """Test case for services_subscriptions_import_put

        Importer les inscriptions des membres aux activités  # noqa: E501
        """
        pass

    def test_sql_post(self):
        """Test case for sql_post

        Exécuter une requête SQL SELECT  # noqa: E501
        """
        pass

    def test_user_categories_get(self):
        """Test case for user_categories_get

        Récupérer la liste des catégories de membres  # noqa: E501
        """
        pass

    def test_user_category_idformat_get(self):
        """Test case for user_category_idformat_get

        Exporter les membres d'une catégorie  # noqa: E501
        """
        pass

    def test_user_iduser_delete(self):
        """Test case for user_iduser_delete

        Supprimer un utilisateur  # noqa: E501
        """
        pass

    def test_user_iduser_get(self):
        """Test case for user_iduser_get

        Récupérer un utilisateur  # noqa: E501
        """
        pass

    def test_user_iduser_post(self):
        """Test case for user_iduser_post

        Mettre à jour un utilisateur  # noqa: E501
        """
        pass

    def test_user_iduser_put(self):
        """Test case for user_iduser_put

        Mettre à jour un utilisateur  # noqa: E501
        """
        pass

    def test_user_import_preview_post(self):
        """Test case for user_import_preview_post

        Prévisualiser un import de membres (POST)  # noqa: E501
        """
        pass

    def test_user_import_preview_put(self):
        """Test case for user_import_preview_put

        Prévisualiser un import de membres  # noqa: E501
        """
        pass

    def test_user_import_put(self):
        """Test case for user_import_put

        Importer une liste de membres  # noqa: E501
        """
        pass

    def test_user_new_post(self):
        """Test case for user_new_post

        Créer un nouveau membre  # noqa: E501
        """
        pass

    def test_web_attachment_pageurifilename_get(self):
        """Test case for web_attachment_pageurifilename_get

        Récupérer un fichier joint d'une page  # noqa: E501
        """
        pass

    def test_web_html_pageuri_get(self):
        """Test case for web_html_pageuri_get

        Récupérer le contenu HTML d'une page  # noqa: E501
        """
        pass

    def test_web_list_get(self):
        """Test case for web_list_get

        Lister les pages du site web  # noqa: E501
        """
        pass

    def test_web_page_pageuri_get(self):
        """Test case for web_page_pageuri_get

        Récupérer les informations d'une page  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
