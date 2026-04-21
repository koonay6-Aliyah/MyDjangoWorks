from django.shortcuts import render
from django.http import HttpResponse
from .models import Book ,Address ,Student #lab7&8
from django.db.models import Q
from .models import Publisher, Lab9_Book, Author
from django.db.models import Count, Sum, Avg, Min, Max, Q
def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html" , {"name": name})  #your render line
def index2(request, val1=0):
    try:
        val1 = int(val1)
        return HttpResponse("value1 = " + str(val1))
    except ValueError:
        return HttpResponse("error, expected val1 to be integer")
def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
def links(request):
    return render(request, 'bookmodule/links.html')
def text_formatting(request):
    return render(request, 'bookmodule/text_formatting.html')
def listing(request):
    return render(request, 'bookmodule/listing.html')
def tables(request):
    return render(request, 'bookmodule/tables.html')
def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765, 'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')
def insert_data(request):
    Book.objects.create(
        title='Continuous Delivery',
        author='J.Humble and D. Farley',
        price=150.00,
        edition=1
    )

    return HttpResponse("Books inserted successfully!")
def insert_data(request):
    if Book.objects.count() == 0:
        Book.objects.create(
            title='Continuous Delivery',
            author='J.Humble and D. Farley',
            price=120.00,
            edition=3
        )
        Book.objects.create(
            title='Reversing: Secrets of Reverse Engineer',
            author='E. Eilam',
            price=97.00,
            edition=2
        ) 
        Book.objects.create(
            title='The Hundred-Page Machine Learning Book',
            author='Andriy Burkov',
            price=100.00,
            edition=4
        )  
        return HttpResponse("3 Books inserted successfully!")
    else:
        return HttpResponse("Books already exist!")

def simple_query(request):
    mybooks = Book.objects.filter(author__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks}) [cite: 55]
    else:
        return render(request, 'bookmodule/index.html')
    
#labe 8
#task one
def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})

#task two
def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})

#task 3
#هنا عكس دالة تاسك 2 
def lab8_task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) & ~Q(title__icontains='qu') & ~Q(author__icontains='qu')
    )
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})

#task 4
#دالة عاديه ترتب الكتب!
def lab8_task4(request):
    #لو برتب العكس !!! احط كذا 
    #order_by('-title')
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})


#task 5
#عرض إجمالي عدد الكتب، مجموع الأسعار، متوسط السعر، وأعلى وأقل سعر
#عشان كذا نادينا مكتبة الماث!!!!!
def lab8_task5(request):
    # حساب الإحصائيات المطلوبة
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})

#task 7
## أضفنا Address و Student هنا
## from .models import Book, Address, Student
def lab8_task7(request):
    # يجيب المدن مع عدد الطلاب المرتبطين بكل مدينة
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab8_task7.html', {'cities': cities})



#lab9
#from .models import Lab9_Book, Publisher, Author
#from django.db.models import Count, Sum, Avg, Min, Max, Q

# Task 1: قائمة الكتب مع نسبة التوفر (Transient Field)

def lab9_task1(request):
    # جلب جميع الكتب
    books = Lab9_Book.objects.all()
    
    # حساب إجمالي عدد الكتب
    total_books = sum(book.quantity for book in books)
    
    # إضافة حقل مؤقت (transient) لكل كتاب
    for book in books:
        book.availability = (book.quantity / total_books) * 100 if total_books > 0 else 0
    
    return render(request, 'bookmodule/lab9_task1.html', {'books': books})



def lab9_task2(request):
    publishers = Publisher.objects.annotate(
        total_stock=Sum('lab9_book__quantity')  # ← quantity مش Count!
    )
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})


from django.db.models import Min

def lab9_task3(request):
    publishers = Publisher.objects.annotate(
        oldest_book_date=Min('lab9_book__pubdate')
    )
    
    # نجيب تفاصيل الكتاب الأقدم لكل ناشر
    for pub in publishers:
        pub.oldest_book = pub.lab9_book_set.order_by('pubdate').first()
    
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})



# Task 4: متوسط، أقل، وأعلى سعر لكل ناشر
def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('lab9_book__price'),
        min_price=Min('lab9_book__price'),
        max_price=Max('lab9_book__price')
    )
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})

# Task 5: الناشرون مع عدد الكتب ذات التقييم العالي (>=4)
def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('lab9_book', filter=Q(lab9_book__rating__gte=4))
    )
    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})

# Task 6: عد الكتب بشروط خاصة (السعر > 50 والكمية بين 1 و 5)
def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        special_count=Count('lab9_book', filter=Q(
            lab9_book__price__gt=50, 
            lab9_book__quantity__gte=1, 
            lab9_book__quantity__lt=5
        ))
    )
    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})




