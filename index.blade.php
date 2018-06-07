@extends('layouts.admin')

@section('content')

<table class="table">
	<thead>
		<th>Revisiones Rápidas</th>
		<th>Opciones</th>
	</thead>


	@foreach($lugares as $sala)
	<tbody>
		<td>
		{{ $sala->nombre }}
		</td>

		<td>
			{!!link_to_route('revisionrap.show', $title = 'Revisiones Rápidas', $parameters = $sala->nombre, $attributes = ['class'=>'btn btn-primary'])!!}
		</td>
	</tbody>
@endforeach

</table>

@endsection
