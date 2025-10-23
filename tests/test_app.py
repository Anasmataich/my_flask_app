from app import create_app

def test_index_page():
    app = create_app()
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

    # تحويل bytes إلى string
    response_text = response.data.decode('utf-8')
    assert "Flask Form" in response_text  # تأكد أن هذه الجملة موجودة في HTML

def test_form_submission():
    app = create_app()
    client = app.test_client()
    response = client.post('/', data={'name': 'Alice'})
    assert response.status_code == 200

    response_text = response.data.decode('utf-8')
    assert "Hello, Alice! Your message has been received." in response_text
