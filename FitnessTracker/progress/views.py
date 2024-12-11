from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from FitnessTracker.progress.forms import LogExerciseForm, LogProgressForm
from FitnessTracker.progress.models import ProgressExercise, ProgressLog


# Create your views here.
class ProgressPageView(LoginRequiredMixin, TemplateView):
    template_name = 'progress/progress.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_exercises = ProgressExercise.objects.filter(
            user=self.request.user
        ).prefetch_related(
            'progress_logs'
        )

        context['exercises'] = [{
            'exercise': exercise,
            'progress_logs': exercise.progress_logs.all()[:5]
        } for exercise in user_exercises]

        return context


class LogExerciseView(LoginRequiredMixin, CreateView):
    model = ProgressExercise
    form_class = LogExerciseForm
    template_name = 'progress/log-exercise.html'
    success_url = reverse_lazy('progress-page')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class LogProgressView(LoginRequiredMixin, TemplateView):
    template_name = 'progress/log-progress.html'

    def dispatch(self, request, *args, **kwargs):
        exercise = get_object_or_404(ProgressExercise, id=self.kwargs['exercise_id'])

        # Check if the exercise belongs to the logged-in user
        if exercise.user != request.user:
            return HttpResponseRedirect(reverse('homepage'))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exercise_id = kwargs.get('exercise_id')
        exercise = get_object_or_404(ProgressExercise, id=exercise_id, user=self.request.user)
        context['exercise'] = exercise
        context['form'] = LogProgressForm()
        return context

    def post(self, request, *args, **kwargs):
        exercise_id = kwargs.get('exercise_id')
        exercise = get_object_or_404(ProgressExercise, id=exercise_id, user=self.request.user)
        form = LogProgressForm(request.POST, exercise=exercise)

        if form.is_valid():
            form.save()
            return redirect('progress-page')

        context = self.get_context_data(**kwargs)
        context['form'] = form

        return self.render_to_response(context)


class LogHistoryView(LoginRequiredMixin, ListView):
    model = ProgressLog
    template_name = 'progress/log-history.html'
    context_object_name = 'progress_logs'

    def dispatch(self, request, *args, **kwargs):
        exercise = get_object_or_404(ProgressExercise, id=self.kwargs['exercise_id'])

        if exercise.user != self.request.user:
            return redirect('homepage')

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        exercise = get_object_or_404(ProgressExercise, id=self.kwargs['exercise_id'])
        return ProgressLog.objects.filter(exercise=exercise)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exercise = get_object_or_404(ProgressExercise, id=self.kwargs['exercise_id'])
        context['exercise'] = exercise
        return context


class LogEditView(LoginRequiredMixin, UpdateView):
    model = ProgressLog
    form_class = LogProgressForm
    template_name = 'progress/log-edit.html'

    def dispatch(self, request, *args, **kwargs):
        log = get_object_or_404(ProgressLog, pk=self.kwargs['pk'])

        if log.exercise.user != request.user:
            return HttpResponseRedirect(reverse('homepage'))

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('log-history', kwargs={'exercise_id': self.object.exercise.id})


class LogDeleteView(LoginRequiredMixin, DeleteView):
    model = ProgressLog
    template_name = 'progress/log-delete.html'

    def dispatch(self, request, *args, **kwargs):
        log = get_object_or_404(ProgressLog, pk=self.kwargs['pk'])

        if log.exercise.user != request.user:
            return HttpResponseRedirect(reverse('homepage'))

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('log-history', kwargs={'exercise_id': self.object.exercise.id})
