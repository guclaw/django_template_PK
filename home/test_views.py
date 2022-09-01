from django.urls import reverse


def test_view_home(client):
    url = reverse('home:home')
    response = client.get(url)

    print("-" * 20)
    print(response)
    print("-" * 20)

    assert response.status_code == 200
    assert '<h1>Home</h1>' in response.content.decode('UTF-8')