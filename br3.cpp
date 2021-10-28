#include<iostream>
#include<stdlib.h>
#include<time.h>
using namespace std;
class Matrix
{
	public:
		int matrix[3][3];
		Matrix(int mat[3][3])
		{
			for(int i=0;i<3;i++)
			{
				for(int j=0;j<3;j++)
				{
					matrix[i][j]=mat[i][j];
		     	}
	
			}
	}

		void print()
		{
			cout<<endl<<endl;
			cout<<"matrix"<<endl;
			for(int i=0;i<3;i++)
			{
				for(int j=0;j<3;j++)
				{
					cout<<matrix[i][j]<<"\t";
					
				}
				cout<<endl;
			}
		}
			friend Matrix operator -(Matrix const &);
						
};
Matrix operator -(Matrix const &m)
{
	Matrix mat=Matrix(m);
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
		{
			mat.matrix[i][j]=-1*mat.matrix[i][j];
			
		}
	}
	return mat;
	
}	
int main()
{
	srand(time(0));
	int mat[3][3];
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
		{
		mat[i][j]=(int)rand();	
		}
		
}
Matrix m=Matrix(mat);
m.print();
m=-m;
m.print();
return 0;
}
