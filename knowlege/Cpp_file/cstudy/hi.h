#include <iostream>
using namespace std;

class Hero{
	public:

	void set_information(double l=100, double w=34, double s=10){
		life = l;
		weapon = w;
		speed = s;
	}

	void get_information(){
		cout<<"life is "<<life<<endl;
		cout<<"spedd is "<<speed<<endl;
		cout<<"weapon is "<<weapon<<endl;
	}

	~Hero(){
		if(speed == 0){
			cout<<"Hero is stopped!"<<endl;
		}else{
			cout<<"Hero is moving!"<<endl;
		}
	}

	private:

	double life;
	double weapon;
	double speed;
};
