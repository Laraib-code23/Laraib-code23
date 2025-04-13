Student={
    "Laraib":{"Science":67,"Math":54,"English":78,"Urdu":87},
      "Aehmad":{"Science":69,"Math":59,"English":58,"Urdu":83},
      "Moon":{"Science":87,"Math":94,"English":38,"Urdu":47}
}
for name,subhjects in Student.items():
    print(f"{name}:")
    for subjects,score in subhjects.items():
        print(f"   {subjects}:{score}")
print()