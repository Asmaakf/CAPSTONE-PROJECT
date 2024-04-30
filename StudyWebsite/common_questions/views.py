from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import QuestionAnswer  # Importing the model
from django.db.models import Q  # Importing Q for conditional filtering in search queries


# Function to create or retrieve support questions and answers
def support_question_answer(request: HttpRequest ):
    if not request.user.is_superuser:
        return render(request, "main/not_allowed.html") # no permission page

    if request.method == "POST":
        try:
            # Collecting data from POST and saving it to the database
            qa = QuestionAnswer(
                question=request.POST["question"],  # Retrieving the question from the form
                answer=request.POST["answer"],  # Retrieving the answer from the form
            )
            qa.save()  # Saving the data
            return redirect('support_question_answer')  # Redirecting to the same page
        except Exception as e:
            # Handling error and printing a message
            print(f"Error occurred while saving question/answer: {e}")

    # If the request is not POST, retrieve all questions and answers to display on the page
    questions_answers = QuestionAnswer.objects.all()

    # Rendering the template with a list of questions and answers
    return render(
        request,
        "common_questions/support_question_answer.html",
        {"questions_answers": questions_answers}  # Sending all questions and answers to the template
    )


# Function to view messages and perform search queries
def view_messages(request):
    # Retrieve all messages from the database
    questions_answers = QuestionAnswer.objects.all()
    
    # Check if there is a search request
    search_query = request.GET.get('q', '')  # Get the search query from parameters
    if search_query:
        # Filter messages based on the query
        # Use Q to search in both the question and the answer
        questions_answers = questions_answers.filter(
            Q(question__icontains=search_query) |  # Search in the question
            Q(answer__icontains=search_query)  # Search in the answer
        )
    
    # Sending the data to the template to display
    return render(request, "common_questions/view_messages.html", {
        'questions_answers': questions_answers,
        'search_query': search_query  # Sending the search query to the template to display in the search form
    })


# Function to delete a question
def delete_question(request, pk):

    if not request.user.is_superuser:
        return render(request, "main/not_allowed.html") # no permission page
    
    try:
         # Retrieve the question based on the primary key
        question=QuestionAnswer.objects.get(pk=pk)
        question.delete()  # Delete the record from the database
    except QuestionAnswer.DoesNotExist:
        return render(request, "main/not_found.html")
    except Exception as e:
        print(e)

    return redirect('common_questions:support_question_answer')  # Redirect to the list of questions


# Function to edit a question
def edit_question(request, pk):

    if not request.user.is_superuser:
        return render(request, "main/not_allowed.html") # no permission page
    
    question =QuestionAnswer.objects.get(pk=pk)
    
    if request.method == 'POST':
        try:
             # Retrieve the updated data from POST
            question.question = request.POST.get('question', '')  # Update the question
            question.answer = request.POST.get('answer', '')  # Update the answer
            question.save()  # Save the changes
        except Exception as e:
            print(e)
    
        # Redirect to the same edit page
        return redirect('common_questions:support_question_answer')  
    
    # If the request is not POST, re-render the edit page
    return render(request, "common_questions/edit_question.html", {'question': question})


