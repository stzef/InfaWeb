from django.views.generic import CreateView, ListView, UpdateView
from django.core.exceptions import ImproperlyConfigured 
from django.db.models.query import QuerySet
from django.utils import six


# Personalizacion de CreateView para incluir using=db
class CustomCreateView(CreateView):

	# String para indicar el alias de la db
	usingAlias = None

	# retorna alias de db
	def get_usignAlias_db(self):
		if self.usingAlias is not None:
			return self.usingAlias
		else:
			if self.request.db is None:
				raise ImproperlyConfigured(
					"Missing request.db"
				)
			else:
				return self.request.db

	# Guarda el objeto desde el formulario 
	def form_valid(self, form):
		usingAlias = self.get_usignAlias_db()

		# Instanciar objeto
		obj = form.save(commit=False)
		# Guardar objeto en la base de datos
		self.object = obj.save(using=usingAlias)

		return super(CustomCreateView, self).form_valid(form)

	# Valida y retorna la clase del formulario
	def get_form_class(self):

		if self.form_class is None:
			raise ImproperlyConfigured(
				"Form class is not specifying."
			)
		else:
			self.form_class

	# retorna el formulario construido
	def get_form(self, form_class=None):
		if self.form_class is None:
			form_class = self.get_form_class()
		else:
			form_class = self.form_class

		# Agregar using a los argumentos de formulario
		kwargs = self.get_form_kwargs()

		if self.usingAlias is not None:
			kwargs['using'] = self.usingAlias
		else:
			kwargs['using'] = self.request.db

		return form_class(**kwargs)


class CustomListView(ListView):

	# String para indicar el alias de la db
	usingAlias = None

	# retorna queryset
	def get_queryset(self):
		if self.queryset is not None:
			queryset = self.queryset
			if isinstance (queryset, QuerySet):
				queryset = queryset.all()
		elif self.model is not None:
			queryset = self.model._default_manager.using(self.get_usignAlias_db()).all()
		else:
			raise ImproperlyConfigured(
				"%(cls)s is missing a QuerySet. Define "
				"%(cls)s.model, %(cls)s.queryset, or override "
				"%(cls)s.get_queryset()." % {
					'cls': self.__class__.__name__
				}
			)

		ordering = self.get_ordering()
		if ordering:
			if isinstance( ordering, six.string_types):
				ordering = ( ordering, )
			queryset = queryset.order_by(*ordering)

		return queryset

	# retorna alias de db
	def get_usignAlias_db(self):
		if self.usingAlias is not None:
			return self.usingAlias
		else:
			if self.request.db is None:
				raise ImproperlyConfigured(
					"Missing request.db"
				)
			else:
				return self.request.db


class CustomUpdateView(UpdateView):

	# String para indicar el alias de la db
	usingAlias = None

	# retorna alias de db
	def get_usignAlias_db(self):
		if self.usingAlias is not None:
			return self.usingAlias
		else:
			if self.request.db is None:
				raise ImproperlyConfigured(
					"Missing request.db"
				)
			else:
				return self.request.db

	# retorna el queryset
	def get_queryset(self):

		if self.queryset is None:
			if self.model:
				return self.model._default_manager.using(self.get_usignAlias_db()).all()
			else:
				raise ImproperlyConfigured(
					"%(cls)s is missing a QuerySet. Define "
					"%(cls)s.model, %(cls)s.queryset, or override "
					"%(cls)s.get_queryset()." % {
						'cls': self.__class__.__name__
					}
				)

		return self.queryset.all()

	# Guarda el objeto desde el formulario 
	def form_valid(self, form):
		usingAlias = self.get_usignAlias_db()

		print "--------------...................---------------------------"
		print usingAlias
		print "--------------...................---------------------------"

		obj = form.save(commit=False)
		self.object = obj.save(using=usingAlias)
		return super(CustomUpdateView, self).form_valid(form)

	# Valida y retorna la clase del formulario
	def get_form_class(self):

		if self.form_class is None:
			raise ImproperlyConfigured(
				"Form class is not specifying."
			)
		else:
			self.form_class

	# retorna el formulario construido
	def get_form(self, form_class=None):
		if self.form_class is None:
			form_class = self.get_form_class()
		else:
			form_class = self.form_class

		# Agregar using a los argumentos de formulario
		kwargs = self.get_form_kwargs()

		if self.usingAlias is not None:
			kwargs['using'] = self.usingAlias
		else:
			kwargs['using'] = self.request.db

		return form_class(**kwargs)
