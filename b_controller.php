<?php

namespace App\Http\Controllers;

//import model _tablename_
use App\Models\_tablename_; 

//import return type View
use Illuminate\View\View;

//import return type redirectResponse
use Illuminate\Http\Request;

//import Http Request
use Illuminate\Http\RedirectResponse;

//import Facades Storage
use Illuminate\Support\Facades\Storage;

class _tablename_Controller extends Controller
{
    /**
     * index
     *
     * @return void
     */
    public function index() : View
    {
        //get all _tablename_Set
        $_tablenameVar_Set = _tablename_::latest()->paginate(10);

        //render view with _tablename_
        return view('_tablename_.index', compact('_tablenameVar_Set'));
    }

    /**
     * create
     *
     * @return View
     */
    public function create(): View
    {
        return view('_tablename_.create');
    }

    /**
     * store
     *
     * @param  mixed $request
     * @return RedirectResponse
     */
    public function store(Request $request): RedirectResponse
    {
        //validate form ... Perbaiki sendiri YAH...
        // $request->validate([
            // 'image'         => 'required|image|mimes:jpeg,jpg,png|max:2048',
            // 'title'         => 'required|min:5',
            // 'description'   => 'required|min:10',
            // 'price'         => 'required|numeric',
            // 'stock'         => 'required|numeric'
        // ]);

        //upload image ... Perbaiki sendiri YAH...
        // $image = $request->file('image');
        // $image->storeAs('public/_tablename_', $image->hashName());

        //create _tablename_
        _tablename_::create([
_Loop1_
        ]);

        //redirect to index
        return redirect()->route('_tablenameVar_.index')->with(['success' => 'Data Berhasil Disimpan!']);
    }
    
    /**
     * show
     *
     * @param  mixed $id
     * @return View
     */
    public function show(string $id): View
    {
        //get _tablename_ by ID
        $_tablenameVar_ = _tablename_::findOrFail($id);

        //render view with _tablename_
        return view('_tablenameVar_.show', compact('_tablenameVar_'));
    }
    
    /**
     * edit
     *
     * @param  mixed $id
     * @return View
     */
    public function edit(string $id): View
    {
        //get _tablename_ by ID
        $_tablenameVar_ = _tablename_::findOrFail($id);

        //render view with _tablename_
        return view('_tablenameVar_.edit', compact('_tablenameVar_'));
    }
        
    /**
     * update
     *
     * @param  mixed $request
     * @param  mixed $id
     * @return RedirectResponse
     */
    public function update(Request $request, $id): RedirectResponse
    {
        //validate form  ... Perbaiki sendiri YAH...
        // $request->validate([
            // 'image'         => 'image|mimes:jpeg,jpg,png|max:2048',
            // 'title'         => 'required|min:5',
            // 'description'   => 'required|min:10',
            // 'price'         => 'required|numeric',
            // 'stock'         => 'required|numeric'
        // ]);

        //get _tablename_ by ID
        $_tablenameVar_ = _tablename_::findOrFail($id);

        // update process
		$_tablenameVar_->update([
_Loop1_
		]);

        //redirect to index
        return redirect()->route('_tablenameVar_.index')->with(['success' => 'Data Berhasil Diubah!']);
    }
	
	/**
     * destroy
     *
     * @param  mixed $id
     * @return RedirectResponse
     */
    public function destroy($id): RedirectResponse
    {
        //get _tablenameVar_ by ID
        $_tablenameVar_ = _tablename_::findOrFail($id);

        //delete image
        // Storage::delete('public/products/'. $product->image);

        //delete _tablenameVar_
        $_tablenameVar_->delete();

        //redirect to index
        return redirect()->route('_tablenameVar_.index')->with(['success' => 'Data Berhasil Dihapus!']);
    }
	
}