
const  movieValidator = document.querySelector('.form_user')

function formValidator(evt) {
    const multipleChoiceForm = document.querySelectorAll('.movie_list')
    if (multipleChoiceForm.length === 0){
        evt.preventDefault();
        alert('You need to select at least one movie')
    }
}
if (!!movieValidator) {
    movieValidator.addEventListener('submit', formValidator)
}


