$(function() {
    'use strict';
    // var _PUBLICATOR_SERVER = 'www.yilmazhuseyin.com:8766';
    var _PUBLICATOR_SERVER = 'www.talkybee.com:8766';
    var $chatInput = $('#chat_input');
    var $chatOutput = $('#chat_output');
    var chatOutput = $chatOutput[0];
    var $userCount = $('#user_count');
    publicator.set_host(_PUBLICATOR_SERVER);
    window.chat = publicator.chat.get_client('yilmazhuseyin');
    chat.onopen(function(res) {
        $chatOutput.val($chatOutput.val() + '\nConnected.');
        $chatInput.keypress(function(e) {
            var k = e.which || e.keyCode;
            if(e.type=='keypress' && k==13) {
                var value = $chatInput.val();
                chat.send_message(value);
                $chatInput.val('');
            }
        });
        var $link = $('#talkybee_link');
        $link.attr('href', 'http://www.talkybee.com/#' + chat.room_code);
        $link.attr('target', '_blank');
    });
    chat.oninfo(function(res) {
        $userCount.text('Online user count: ' + _.keys(chat.users).length);
    });
    chat.onmessage(function(res) {
        var msg = res.nick + '-' + res.data;
        $chatOutput.val($chatOutput.val() + '\n' + msg);
        chatOutput.scrollTop = chatOutput.scrollHeight;
    });
    chat.onerror(function(res) {
        return console && console.log && console.log('onerror', res);
    });
});
