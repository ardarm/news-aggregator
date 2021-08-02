function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

$(document).ready(function() {
    console.log( "ready!" );
    element = document.getElementsByClassName("text-muted");
    for (i = 0; i < element.length; i++) {
        t = document.getElementsByClassName("text-muted")[i].innerText;
        var d = new Date(t);
        document.getElementsByClassName("text-muted")[i].innerText = d.toDateString();
    }

    $(".bookmark").change(function () {
      article = $(this).attr("articleurl");
      checked = $(this).attr("checked");
      $.ajax({
        url: 'bookmark/',
        data: {
          'article': article,
          'checked': checked
        }
      });
    });
});
