from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie
# quam lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla
# eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget
# consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi,
# pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna, non
# finibus neque cursus id.
def index(request):
    """Main index view of the website"""
    return render(request, "oc_lettings_site/index.html")


def custom_404(request, exception):
    """Custom error 404 handling view"""
    return render(request, "oc_lettings_site/errors/404.html", status=404)


def custom_500(request):
    """Custom error 500 handling view"""
    return render(request, "oc_lettings_site/errors/500.html", status=500)
