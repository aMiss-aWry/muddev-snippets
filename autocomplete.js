/*
 * Evennia Webclient Input Auto Completion plugin
 * Housed in /web/static/webclient/js/plugins/autocomplete.js
 * Attempts to complete user input. Tab through array given by {'type': 'autocomplete'} from the game.
 * Set up:
 *    <script src={% static "webclient/js/plugins/autocomplete.js" %} language="javascript" type="text/javascript"></script>
 *    1) Add the above line to your web/templates/webclient/base.html where the other plugins are
 *    2) The autocomplete code expects a list of commands (or anything else you want to replace the input with).
 *       so send it as a msg(list_as_string, {'type': 'autocomplete'}) (or fiddle with your msg/parsing as needed)
 * To test without coding the whole autocomplete function, once you do the above, you can:
 *    py self.msg(("['if this works right it will show up in your input field!']", {'type':'autocomplete'}))
 */

let autocomplete = (function () {
    var options = new Array();
    var i = 0;
    var tabdown = false;  // ignores when tab is held down; remove refs to this if you want held-down tabs to continue the cycle
    var current_input = '';
    var original_input = '';

    // Step forward through the options array, looping back to the beginning at the end
    var next = function () {
        inputfield = input();
        inputfield.val("");
        inputfield.blur().focus().val(options[i]);
        if (i+1 >= options.length) {
            i = 0;
        } else {
            i++;
        }
    }

    var input = function () {
        // Replace text in input, move cursor to end of new value. Save old input
        var inputfield = $(".inputfield:focus");
        if( inputfield.length < 1 ) { // focus the default (last), if nothing focused
            inputfield = $(".inputfield:last");
        }
        if( inputfield.length < 1 ) { // pre-goldenlayout backwards compatibility
            inputfield = $("#inputfield");
        }
        return inputfield;
    }

    //
    // Handle tab button event.
    var onKeydown = function(event) {
        var code = event.which;

        // Process tab press
        if (code === 9) { // Tab press
            event.preventDefault();
            if (!tabdown) {
                // Clear saved info on initial tab press
                tabdown = true;
            } else {  // Do not allow holding down
                return;
            }
        } else {
            original_input = '';
            options = null;
            i = 0;
            return;
        }
        inputfield = input();
        var line = inputfield.val();
        if( line !== "") {
            if (original_input == "" || !line.startsWith(original_input)) {  // Check new text against potential commands
                original_input = line;
                Evennia.msg("text", ['test2 ' + original_input], {});  // This is the message that requests that the game server send back an autocomplete message.
                                                                       // You would replace it with the equivalent on your end. 'test2' is my test command.
            }
            if (options && options.length) {
                next();
            }
            return;
        }
    }

    var onText = function (args, kwargs) {
        var msgtype = kwargs == null ? 'out' : kwargs['type'];
        if (args == null) {
            return;
        }
        if (msgtype == 'autocomplete') {
            args = args[0].toString().replaceAll("'", '"')  // The weirdness of converting python list-as-string to JSON-parseable string-that-is-list.
            options = JSON.parse(args)
            if (options && options.length) {
                next();  // Replace the text in input box with guess
            }
        }
        return;
    }

    var onKeyup = function(event) {
        // Process tab release. Tab doesn't work well with onKeyup, hence this general solution. 'solution'
        if (tabdown === true) {
            tabdown = false;
        }
        return;
    }

    return {
        init: function () {},
        onKeydown: onKeydown,
        onKeyup: onKeyup,
        onText: onText,
    }
})();
window.plugin_handler.add("autocomplete", autocomplete);
