/**
 * Created by johnmachahuay on 6/26/15.
 */

angular
    .module('app')
    .constant('END_POINT', {
        loginClient: '/login/',
        logoutClient: '/logout/',

        getListModuleCampaign: '/campaign/list/',
        createModuleCampaign: '/campaign/create/',
        getModuleCampaign: '/campaign/get/mailing_id/',
        getStatisticsModuleCampaign: '/campaign/mailing_id/statistics/',
        updateModuleCampaign: '/campaign/update/mailing_id/',
        deleteModuleCampaign: '/campaign/delete/mailing_id/',

        getListModuleTemplate: '/template/list/',
        createModuleTemplate: '/template/create/',
        getModuleTemplate: '/template/get/module_template_id/',
        updateModuleTemplate: '/template/update/module_template_id/',
        deleteModuleTemplate: '/template/delete/module_template_id/',
        getListGeneralTemplate: '/template/general-list/',

        getListModuleBD: '/bd/list/',
        createModuleBD: '/bd/create/',
        getModuleBD: '/bd/get/module_db_id/',
        updateModuleBD: '/bd/update/module_db_id/',
        deleteModuleBD: '/bd/delete/module_db_id/',
        deleteContactsModuleBD: '/bd/delete-contacts/module_db_id/',
        importContactToBD: '/bd/import-csv/module_db_id/',
        addContactToBD: '/bd/module_db_id/add-contact/'
    });