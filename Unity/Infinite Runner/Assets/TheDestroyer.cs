using System.Collections;
using UnityEngine;

public class TheDestroyer : MonoBehaviour
{

    private float timer = 0.0f;

    // Update is called once per frame
    void Update()
    {
        timer += Time.deltaTime;
        if (timer > 5)
        {
            Destroy(gameObject);
        }
    }
}
