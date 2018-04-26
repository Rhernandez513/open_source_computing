from unittest import mock
from unittest.mock import Mock

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from polls.models import Question, Choice


class QuestionModelTestCase(TestCase):
    def setUp(self):
        question1 = Question.objects.create(question_text='hello how are you?', pub_date=timezone.now())
        question2 = Question.objects.create(question_text='hello how are you second?', pub_date=timezone.now())
        Choice.objects.create(question=question1, choice_text='one', votes=3)
        Choice.objects.create(question=question1, choice_text='two', votes=7)
        Choice.objects.create(question=question1, choice_text='three', votes=10)

    def test_question_saving(self):
        first_question = Question.objects.get(question_text='hello how are you?')
        second_question = Question.objects.get(question_text='hello how are you second?')
        self.assertIsNotNone(first_question)
        self.assertIsNotNone(second_question)

    def test_total_questions(self):
        questions = Question.objects.all().count()
        self.assertEqual(questions, 2)

    def test_number_of_choice(self):
        choices_count = Question.objects.get(question_text='hello how are you?').choice_set.all().count()
        self.assertEqual(choices_count, 3)

    def test_number_of_choice_with_votes_greater_then_5(self):
        choices_count = Question.objects.get(question_text='hello how are you?').choice_set.filter(votes__gt=5).count()
        self.assertEqual(choices_count, 2)


class IndexViewTestCase(TestCase):
    def test_index_view_status(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_context(self):
        response = self.client.get(reverse('index'))
        response_text = ''
        for resp in response.context:
            if resp.get('response'):
                response_text = resp.get('response')

        self.assertEqual(response_text, "Hello World, You're looking at the polls index.")


class TwitterViewTestCase(TestCase):
    def twitter_mock_method(self, question):
        return 'twitter response'

    def test_twitter_view_status(self):
        with mock.patch('polls.twitter_interface.tweet_api.GetSearch', new=self.twitter_mock_method):
            response = self.client.get(reverse('twitter_results', args=[1]))
            self.assertEqual(response.status_code, 200)

    def test_twitter_view_context(self):
        with mock.patch('polls.twitter_interface.tweet_api.GetSearch', new=self.twitter_mock_method):
            response = self.client.get(reverse('twitter_results', args=[1]))
            response_text = ''
            for resp in response.context:
                if resp.get('twitter_reponse'):
                    response_text = resp.get('twitter_reponse')

            self.assertEqual(response_text, "twitter response")


class RedItViewTestCase(TestCase):
    def redit_mock_method(self, question, limit=5):
        return_data = []
        for i in range(5):
            return_data.append("Dummy Data")
        return return_data

    def test_redit_view_status(self):
        with mock.patch('polls.reddit_interface.reddit_api.search', new=self.redit_mock_method):
            response = self.client.get(reverse('reddit_results', args=[1]))
            self.assertEqual(response.status_code, 200)

    def test_redit_view_context(self):
        with mock.patch('polls.reddit_interface.reddit_api.search', new=self.redit_mock_method):
            response = self.client.get(reverse('reddit_results', args=[1]))
            response_text = ''

            for resp in response.context:
                if resp.get('reddit_response'):
                    response_text = resp.get('reddit_response')

            self.assertEqual(len(response_text), 5)


class WikiViewTestCase(TestCase):
    def wiki_mock_method(self, question):
        data = Mock()
        data.page = 'Wiki response'
        return data

    def test_wiki_view_status(self):
        with mock.patch('polls.wikipedia_interface.api.page', new=self.wiki_mock_method):
            response = self.client.get(reverse('wiki_results', args=[1]))
            self.assertEqual(response.status_code, 200)

    def test_wiki_view_context(self):
        with mock.patch('polls.wikipedia_interface.api.page', new=self.wiki_mock_method):
            response = self.client.get(reverse('wiki_results', args=[1]))
            response_object = ''
            for resp in response.context:
                if resp.get('wiki_response'):
                    response_object = resp.get('wiki_response')

            self.assertIsNotNone(response_object)


class IMDBViewTestCase(TestCase):
    def imdb_mock_method(self, question):
        return 'imdb response'

    def test_imdb_view_status(self):
        with mock.patch('polls.imdb_interface.imdb.search_for_title', new=self.imdb_mock_method):
            response = self.client.get(reverse('imdb_results', args=[1]))
            self.assertEqual(response.status_code, 200)

    def test_imdb_view_context(self):
        with mock.patch('polls.imdb_interface.imdb.search_for_title', new=self.imdb_mock_method):
            response = self.client.get(reverse('imdb_results', args=[1]))
            response_text = ''
            for resp in response.context:
                if resp.get('result'):
                    response_text = resp.get('result')

            self.assertEqual(response_text, "imdb response")
