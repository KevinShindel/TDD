from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from lists.models import Item
from lists.views import home_page


class HomePageTest(TestCase):
    '''home page test'''

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html lang="en">'), html)
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Second item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items.first()
        last_saved_item = saved_items.last()

        self.assertEqual(first_saved_item.text, 'The first item')
        self.assertEqual(last_saved_item.text, 'Second item')


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/shared/')
        self.assertTemplateUsed(response, 'shared.html')

    def test_display_all_items(self):
        item1 = Item.objects.create(text='item 1')
        item2 = Item.objects.create(text='item 2')

        response = self.client.get('/lists/shared/')
        self.assertContains(response, item1.text)
        self.assertContains(response, item2.text)


class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new/', data={'item_text': 'A new list item'})
        self.assertRedirects(response, '/lists/shared/')
