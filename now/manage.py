from nowstargm import app,db
from flask_script import Manager
from nowstargm.models import User,Image,Comment
import random
manager = Manager(app=app)

# def get_image_url():
#     return 'https://images.nowcoder.com/head/'+str(random.randint(0,1000))+'m.png'



@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    # for i in range(0,100):
    #     db.session.add(User('User'+str(i+1),'a'+str(i)))
    #     for j in range(0,10):
    #         db.session.add(Image(get_image_url(),i+1))
    #         for k in range(0,3):
    #             db.session.add(Comment('This is a comment'+str(k+1),1+10*i+j,i+1))


    #
    # db.session.commit()

    # User.query.filter_by(id=2).update({'username':'[New2]'})
    # image_id = Image.query(id).order_by(db.desc(Image.id)).limit(10)



    if __name__ == '__main__':
        manager.run()