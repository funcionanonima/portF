document.addEventListener('DOMContentLoaded', function() {
    var elems1 = document.querySelectorAll('.dropdown-trigger');
    var elems2 = document.querySelectorAll('.sidenav');
    var instances = M.Dropdown.init(elems1);
    var instances = M.Sidenav.init(elems2);
  });