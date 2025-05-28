Method overriding:


1. Create Parent class Physics and sub class Topic1 and Topic2. add methods to display Auther Name and Topic name using method overriding
'''


class Physics:
    def display(self):
        print("auther name=""H.C.Varma")


class Topic1(Physics):
     def show(self):
        super().display()
        topic_name="wave option"
        print("topic name1=",topic_name)


class Topic2(Topic1):
     def show(self):
         super().display()
         topic_name="current electricity"
         print("topic2 name=",topic_name)


obj=Topic1()
obj.show()


s=Topic2()
s.show()


