
odoo.define('mpesa_payment.main', function (require) {
"use strict";

var chrome = require('mpesa_payment.chrome');
var core = require('web.core');

core.action_registry.add('pos.ui', chrome.Chrome);

});
