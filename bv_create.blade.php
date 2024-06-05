@extends('layout.admin.base')
@section('isi')

    <div class="container mt-5 mb-5">
        <div class="row">
            <div class="col-md-12">
			    <h1>_tablename_ - Data Baru</h1>
                <div class="card border-0 shadow-sm rounded">
                    <div class="card-body">
                        <form action="{{ route('_tablenameVar_.store') }}" method="POST" >
                            @csrf                        
_Loop1_

                            <button type="submit" class="btn btn-md btn-primary me-3"><i class="fa-regular fa-floppy-disk"></i> SIMPAN</button>
                            <button type="reset" class="btn btn-md btn-warning"><i class="fa-solid fa-arrow-rotate-left"></i> RESET</button>
                        </form> 
                    </div>
                </div>
            </div>
        </div>
    </div>

@endsection

@section('skrip')
    <script>        
    </script>
@endsection

