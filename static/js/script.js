$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown({ hover: false });
    $('.tabs').tabs();
    $('.datepicker').datepicker({
      format: 'd mmm, yyyy',
      yearRange: 2,
      showClearBtn: true,
      i18n: {
        done: "select"
      }
    });
    $('.parallax').parallax();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.carousel').carousel({
        indicators: true});
    $('.modal').modal();
  

     /* Code used from Task Manager course material */

     validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    } 
  });

/* Checking password and confirm Password are the same */
function Validate() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;
    if (password != confirmPassword) {
        alert("Passwords do not match!");
        return false;
    }
    return true;
}


/* https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_toggle_password 

Showing Password Input */
function showPassword() {
    let p = document.getElementById("password");
    if (p.type  === "password") {
        p.type = "text";
    } else {
        p.type = "password";
    } 
    let cp = document.getElementById("confirmPassword");
    if (cp.type === "password") {
        cp.type = "text";
    } else {
        cp.type = "password";
    } 
}

function loginPassword() {
    let pEnter = document.getElementById("password_enter");
    if (pEnter.type === "password") {
        pEnter.type = "text";
    } else {
        pEnter.type = "password";
    } 
}

