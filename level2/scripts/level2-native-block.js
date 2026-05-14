Java.perform(function () {
  console.log("attached");

  var MainActivity = Java.use("sg.vantagepoint.uncrackable2.MainActivity");
  var CodeCheck = Java.use("sg.vantagepoint.uncrackable2.CodeCheck");

  MainActivity.init.implementation = function () {
    console.log("init intercepted - BLOCKING native call");

    return;
  };

  CodeCheck.bar.implementation = function (input) {
    console.log("bar intercepted - BLOCKING native call");
    return true;
  };
});
