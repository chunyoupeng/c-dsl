#include <stdio.h>

//@racket
typedef struct {
    char name[50];          // 火箭的名称
    double height;          // 火箭的高度（米）
    double weight;          // 火箭的重量（千克）
    double thrust;          // 火箭的推力（牛顿）
    double fuelCapacity;    // 燃料容量（升）
    int numberOfEngines;    // 发动机数量
    char engineType[30];    // 发动机类型
    double maxAltitude;     // 最大飞行高度（米）
    char missionType[50];   // 任务类型（例如，载人、卫星发射等）
    bool isReusable;        // 是否可重复使用
} Rocket;


int getRacket(){
  return 0;
}

//@missile
typedef struct {
    char name[50];         // 导弹的名称
    double length;         // 导弹的长度（米）
    double diameter;       // 导弹的直径（米）
    double weight;         // 导弹的重量（千克）
    double range;          // 射程（千米）
    double speed;          // 速度（马赫）
    char warheadType[30];  // 弹头类型
    double warheadWeight;  // 弹头重量（千克）
    char guidanceSystem[50]; // 导引系统
} Missile;


int main(){
  // 这里调用
  printf("Hello, Racket!\n");
};

