$( document ).ready(function() {
    $('.close').click(function() {
        $('#ergebnis').hide();
        document.getElementById('selectCountry').value='none';
        map.deselect(map.selectedRegions[0]);
    });
    $('select').change(function () {
        if ($('select option:selected').val()=='none') {
            $('#ergebnis').hide();
            map.deselect(map.selectedRegions[0]);
        } else {
            var code = $('select option:selected').val();
            var land = map.selectedRegions[0]
            $('#ergebnis').hide();
            $('.contactItem').hide();
            $('#countryUeberschrift').text(land);
            if ($('.contact-' + code).length > 0) {
                $('#ergebnis').show();
                $('.contact-' + code).show();
            }
            document.getElementById('selectCountry').value=code;
        }
    });
});