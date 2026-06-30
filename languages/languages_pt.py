pt = {
    "starthandler": {
        "text": "Bem-vindo! Por favor, selecione uma opção:",
        "keyboard": [
            {"text": "Selecionar Assinaturas de Canais", "callback_data": "buychannelsubscriptions"},
            {"text": "Selecionar Idioma", "callback_data": "select_language"}
        ]
    },
    "selectlanguagehandler": {
        "text": "Por favor, selecione um idioma:",
        "keyboard": [
            {"text": "English", "callback_data": "en"},
            {"text": "فارسی", "callback_data": "fa"},
            {"text": "Español", "callback_data": "es"},
            {"text": "Deutsch", "callback_data": "de"},
            {"text": "Русский", "callback_data": "ru"},
            {"text": "日本語", "callback_data": "ja"},
            {"text": "中文", "callback_data": "zh"},
            {"text": "Français", "callback_data": "fr"},
            {"text": "Türkçe", "callback_data": "tr"},
            {"text": "Italiano", "callback_data": "it"},
            {"text": "Português", "callback_data": "pt"},
            {"text": "Nederlands", "callback_data": "nl"}
        ]
    },
    "setlanguagehandler": {
        "text": "Seu idioma foi alterado para Português."
    },
    "selectchannelsubscriptionstate": {
        "text": "Escolha seu canal."
    },
    "selectsubscriptionsstate": {
        "text": "Escolha sua assinatura."
    },
    "selectcryptostate": {
        "text": "Escolha sua criptomoeda."
    },
    "sendpaymentlinkstate": {
        "text": "Use o link abaixo para efetuar o pagamento."
    },
    "checkpaymentstatusstate": {
        "text": "Clique no botão abaixo para verificar o status do pagamento.\nID da fatura:",
        "keyboard": [
            {"text": "Verificar Status do Pagamento", "callback_data": ""}
        ]
    },
    "cancel": {
        "text": "Seu pagamento foi cancelado ou expirou por inatividade.\nPor favor, tente novamente."
    },
    "joinrequesthandler": {
        "text": "Seu pedido de ingresso foi recebido. Aguarde a aprovação."
    },
    "addadminhandler": {
        "text": "Por favor, forneça o ID do usuário para conceder privilégios de administrador."
    },
    "addspecialuserhandler": {
        "text": "Por favor, forneça o ID do usuário para marcar como especial."
    },
    "banuserhandler": {
        "text": "Por favor, forneça o ID do usuário para banir."
    },
    "checkpaymentstatushandler": {
        "text": "Verificando status do pagamento. Aguarde..."
    },
    "adminpannelhandler": {
        "text": """
Guia de Comandos do Painel Administrativo:

1. **Adicionar Canal Obrigatório**: Use `/addjoinforcechannel` para adicionar um canal obrigatório.
2. **Excluir Canal Obrigatório**: Use `/deletejoinforcechannel` para remover um canal obrigatório.
3. **Adicionar Canal**: Use `/addchannel` para adicionar um novo canal.
4. **Excluir Canal**: Use `/deletechannel` para excluir um canal existente.
5. **Adicionar Assinatura**: Use `/addsubscription` para criar uma nova assinatura para um canal.
6. **Excluir Assinatura**: Use `/deletesubscription` para remover uma assinatura existente.
7. **Banir Usuário**: Use `/banuser` para banir um usuário do sistema.
8. **Desbanir Usuário**: Use `/unbanuser` para desbanir um usuário previamente banido.
9. **Adicionar Administrador**: Use `/addadmin` para conceder privilégios de administrador a um usuário.
10. **Remover Administrador**: Use `/removeadmin` para revogar privilégios de administrador.
11. **Mostrar Todos os Administradores**: Use `/showalladmin` para listar todos os administradores do sistema.
12. **Adicionar Usuário Especial**: Use `/addspecialuser` para marcar um usuário como especial.
13. **Remover Usuário Especial**: Use `/removespecialuser` para remover o status especial de um usuário.
14. **Exportar Tabela para CSV**: Use `/exporttabletocsv` para exportar uma tabela do banco de dados para um arquivo CSV.

Digite o comando correspondente para executar a ação desejada.
"""
    },
    "selectchannelsubscriptions": {
        "text": "Por favor, selecione seu canal."
    },
    "unbanuserhandler": {
        "text": "Por favor, forneça o ID do usuário para desbanir."
    },
    "removeadminhandler": {
        "text": "Por favor, forneça o ID do usuário para remover privilégios de administrador."
    },
    "showalladminhandler": {
        "text": "Aqui está a lista de todos os administradores do sistema."
    },
    "removespecialuserhandler": {
        "text": "Por favor, forneça o ID do usuário para remover dos usuários especiais."
    },
    "exporttabletocsvhandler": {
        "text": "Por favor, forneça o nome da tabela para exportar como arquivo CSV."
    },
    "addforcedjoinchannelhandler": {
        "text": "Por favor, forneça os detalhes do canal a ser adicionado como obrigatório."
    },
    "deleteforcedjoinchannelhandler": {
        "text": "Por favor, forneça os detalhes do canal a ser removido da lista obrigatória."
    },
    "addchannelhandler": {
        "text": "Por favor, forneça os detalhes do canal a ser adicionado."
    },
    "deletechannelhandler": {
        "text": "Por favor, forneça os detalhes do canal a ser excluído."
    },
    "addsubscriptionhandler": {
        "text": "Por favor, forneça os detalhes da assinatura a ser adicionada."
    },
    "deletesubscriptionhandler": {
        "text": "Por favor, forneça os detalhes da assinatura a ser excluída."
    },
    "forcejoincheckerhandler": {
        "text": "Para usar o bot, junte-se aos seguintes canais e grupos:"
    },
    "confirmdeletestate": {
        "text": "Canal excluído com sucesso."
    },
    "deleteforcedjoinchannelstate": {
        "text": "Selecione um canal para excluir."
    },
    "confirmdeletechannelstate": {
        "text": "Canal excluído com sucesso."
    },
    "deletechannelstate": {
        "text": "Selecione um canal para excluir."
    },
    "deletesubscriptionstate": {
        "text": "Selecione uma assinatura para excluir."
    },
    "listsubscriptionsstate": {
        "text": "Escolha sua assinatura."
    },
    "confirmdeleteanotherstate": {
        "text": "Assinatura excluída.\nDeseja excluir outra?"
    },
    "DeleteAnotherSubscriptionState": {
        "text": "Escolha sua assinatura."
    },
    "showlistoftableshandler": {
        "text":
            "1. canais\n"
            "2. assinaturas\n"
            "3. usuario2assinaturas\n"
            "4. usuáriosespeciais\n"
            "5. pagamentos\n"
            "6. uniãoforçada\n"
            "7. usuários"
    },
    "addchannelstate": {
        "text": "Envie o link do canal."
    },
    "getchatidstate": {
        "text": "Canal adicionado com sucesso."
    },
    "addforcedjoinchannelstate": {
        "text": "Envie o link do canal."
    },
    "getchannellinkstate": {
        "text": "Canal adicionado com sucesso."
    },
    "getchannelhandler": {
        "text": "Selecione um canal para marcar o usuário como especial."
    },
    "addsubscriptionstate": {
        "text": "Escolha seu canal."
    },
    "getnamestate": {
        "text": "Digite o nome da assinatura."
    },
    "getpriceState": {
        "text": "Digite o preço em dólares."
    },
    "getdaystate": {
        "text": "Digite o número de dias para a assinatura."
    },
    "confirmaddanotherstate": {
        "text": "Assinatura criada. Deseja adicionar outra?"
    },
    "selectsubscriptionstate": {
        "text": "Escolha sua assinatura."
    }
}
