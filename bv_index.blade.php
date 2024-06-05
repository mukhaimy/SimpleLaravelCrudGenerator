@extends('layout.admin.base')
@section('isi')
    <div class="container mt-5">
        <div class="row">
            <div class="col-md-12">
                <h1>_tablename_</h1>
				
                <div class="card border-0 shadow-sm rounded">
                    <div class="card-body">
                        <a href="{{ route('_tablenameVar_.create') }}" class="btn btn-md btn-success mb-3"><i class="fa-solid fa-plus"></i> Data Baru</a>
                        <table class="table ">
                            <thead>
                                <tr>
									<th style="width: 140px"></th>
_Loop1_
                                </tr>
                            </thead>
                            <tbody>
                                @forelse ($_tablenameVar_Set as $_tablenameVar_)
                                    <tr>
                                        <td class="text-center">
                                            <form onsubmit="return confirm('Apakah Anda Yakin untuk Menghapus Data: {{ $_tablenameVar_->_delField_ }}?');" action="{{ route('_tablenameVar_.destroy', $_tablenameVar_->id) }}" method="POST">
                                                <a href="{{ route('_tablenameVar_.show', $_tablenameVar_->id) }}" class="btn btn-sm btn-dark"><i class="fa-solid fa-magnifying-glass"></i></a>
                                                <a href="{{ route('_tablenameVar_.edit', $_tablenameVar_->id) }}" class="btn btn-sm btn-primary"><i class="fa-solid fa-pen"></i></a>
                                                
                                                @csrf
                                                @method('DELETE')
                                                <button type="submit" class="btn btn-sm btn-danger"><i class="fa-solid fa-trash"></i></button>
                                            </form>
                                        </td>
_Loop2_                                        
                                    </tr>
                                @empty
                                    <div class="alert alert-danger">
                                        Data belum Tersedia.
                                    </div>
                                @endforelse
                            </tbody>
                        </table>
                        {{ $_tablenameVar_Set->links() }}
                    </div>
                </div>
            </div>
        </div>
    </div>

@endsection

@section('skrip')
    <script>
        //message with sweetalert
        @if(session('success'))
            Swal.fire({
                icon: "success",
                title: "BERHASIL",
                text: "{{ session('success') }}",
                showConfirmButton: false,
                timer: 2000
            });
        @elseif(session('error'))
            Swal.fire({
                icon: "error",
                title: "GAGAL!",
                text: "{{ session('error') }}",
                showConfirmButton: false,
                timer: 2000
            });
        @endif

    </script>
@endsection