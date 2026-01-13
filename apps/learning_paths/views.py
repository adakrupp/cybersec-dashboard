from django.views.generic import ListView, DetailView
from .models import LearningPath, SkillNode


class LearningPathListView(ListView):
    """Display all available learning paths"""
    model = LearningPath
    template_name = 'learning_paths/list.html'
    context_object_name = 'paths'

    def get_queryset(self):
        return LearningPath.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Learning Paths'
        return context


class LearningPathDetailView(DetailView):
    """Display interactive skill tree for a specific path"""
    model = LearningPath
    template_name = 'learning_paths/detail.html'
    context_object_name = 'path'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'{self.object.name} - Learning Path'

        # Get all nodes for this path with related data
        nodes = SkillNode.objects.filter(
            learning_path=self.object
        ).prefetch_related(
            'prerequisites',
            'resources',
            'tools',
            'certifications'
        )

        context['nodes'] = nodes

        # Build graph data structure for visualization
        graph_data = {
            'nodes': [],
            'edges': []
        }

        for node in nodes:
            graph_data['nodes'].append({
                'id': node.id,
                'label': node.title,
                'difficulty': node.difficulty,
                'hours': node.estimated_hours,
                'description': node.description,
            })

            # Add edges for prerequisites
            for prereq in node.prerequisites.all():
                graph_data['edges'].append({
                    'from': prereq.id,
                    'to': node.id
                })

        context['graph_data'] = graph_data
        return context
