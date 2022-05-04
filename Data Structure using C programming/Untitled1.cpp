#include<iostream>

using namespace std;

struct educ
{
   int cllg_id;
   string cllg_name;
};

struct std
{
  int roll_no;
  string name;
  educ education;
};
struct std a;
int main()
{
   a.roll_no=43;
   a.name="Pragya";
   a.education.cllg_id=27302;
   a.education.cllg_id="PSIT";
   
   cout<<"Details"<<endl;
   cout<<"Roll.no: "<<a.roll_no<<endl<<"Name: "<<a.name<<endl<<"Collge ID: "<<a.education.cllg_id<<endl<<"College Name: "<<a.education.cllg_name<<endl;
   
   return 0;
}
