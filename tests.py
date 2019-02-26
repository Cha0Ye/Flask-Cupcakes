from app import app
from models import db, connect_db, Cupcakes
import unittest

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_cupcake'
app.config['SQLALCHEMY_ECHO'] = False

db.create_all()


class Our_Integration_Test(unittest.TestCase):
    def setUp(self):
        """Set up test client and make new cupcakes."""

        Cupcakes.query.delete()

        self.client = app.test_client()
        new_cupcake = Cupcakes(id=10000,
                               flavor='Blueberry',
                               size='medium',
                               rating=9.3,
                               image='http://images.media-allrecipes.com/userphotos/960x960/4482229.jpg')
        db.session.add(new_cupcake)
        db.session.commit()

    def test_all_cupcakes(self):
        """/cupcakes should show all cupcakes"""
        response = self.client.get("/cupcakes")
        response_data = response.json['response']
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]['flavor'], 'Blueberry')
        self.assertEqual(response_data[0]['size'], 'medium')
        self.assertEqual(response_data[0]['rating'], 9.3)
        self.assertEqual(response_data[0]['image'], 'http://images.media-allrecipes.com/userphotos/960x960/4482229.jpg')
        self.assertEqual(response.status_code, 200)
        # end test_all

    # def test_get_single_cupcake(self):
    #     response = self.client.get("/cupcakes/10000")
    #     self.assertEqual(response.json['response']['flavor'], 'Blueberry')
    #     self.assertEqual(response.json['response']['size'], 'medium')
    #     self.assertEqual(response.json['response']['rating'], 9.3)
    #     self.assertEqual(response.json['response']['image'], 'http://images.media-allrecipes.com/userphotos/960x960/4482229.jpg')
    #     self.assertEqual(response.status_code, 200)

    def test_add_cupcake(self):
        """/cupcakes method POST should add a new cupcake"""
        response = self.client.post(
            "/cupcakes",
            json={"flavor": "Strawberry",
                  "size": 'small',
                  "rating": 9.5,
                  "image": "https://cdn.cpnscdn.com/static.coupons.com/ext/kitchme/images/recipes/800x1200/fresh-strawberry-cupcakes-cream-cheese-frosting_44071.jpg"
                  })

        self.assertEqual(response.json['response']['flavor'], 'Strawberry')
        self.assertEqual(response.json['response']['size'], 'small')
        self.assertEqual(response.json['response']['rating'], 9.5)
        self.assertEqual(response.json['response']['image'], "https://cdn.cpnscdn.com/static.coupons.com/ext/kitchme/images/recipes/800x1200/fresh-strawberry-cupcakes-cream-cheese-frosting_44071.jpg")

        self.assertEqual(response.status_code, 200)

        # Testing to see if a resource was added to database.

        response = self.client.get("/cupcakes")
        response_data = response.json['response']
        self.assertEqual(len(response_data), 2)
