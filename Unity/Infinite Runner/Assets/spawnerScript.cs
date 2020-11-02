using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class spawnerScript : MonoBehaviour
{

    public GameObject[] obstacles;
    private float timeBetweenSpawn;
    public float startTimeBtwSpawn;
    public float decreaseTime;
    public float minTime;

    

    // Update is called once per frame
    void Update()
    {
        if (timeBetweenSpawn <= 0)
        {
            int rand = Random.Range(0, obstacles.Length);
            Instantiate(obstacles[rand], transform.position, Quaternion.identity);
            timeBetweenSpawn = startTimeBtwSpawn;
            if (startTimeBtwSpawn > minTime)
            {
                startTimeBtwSpawn -= decreaseTime;
            }

        }
        else{
            timeBetweenSpawn -= Time.deltaTime;
        }
    }
}
