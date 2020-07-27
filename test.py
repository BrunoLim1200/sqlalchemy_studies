from models import People, db_session

def new_peoples():
    people = People(name='Jorge',age=22)
    print(people)
    people.save()

def check_peoples():
    people = People.query.all()
    print(people)
    #people = People.query.filter_by(name='Jorge').first()
    #print(people.age)

def change_peoples():
    people = People.query.filter_by(name='Jorge').first()
    people.age = 21
    people.save()

def delete_peoples():
    people = People.query.filter_by(name='Jorge').first()
    people.delete()

if __name__ == '__main__':
    new_peoples()
    #delete_peoples()
    #check_peoples()
    #change_peoples()