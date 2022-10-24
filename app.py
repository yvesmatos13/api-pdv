#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask, Blueprint
from controle.lojaControle import loja_blueprint
from controle.meioPagamentoControle import meioPagamento_blueprint

app = Flask(__name__)
app.register_blueprint(loja_blueprint, url_prefix='/loja')
app.register_blueprint(meioPagamento_blueprint, url_prefix='/meioPagamento')
app.config['JSON_SORT_KEYS'] = False